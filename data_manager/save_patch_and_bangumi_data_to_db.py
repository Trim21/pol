import json
import pathlib
from os import path

import tqdm

from app.db import database
from app.db_models import BangumiSource, MissingBangumi

base_dir = pathlib.Path(path.dirname(__file__))

# data = requests.get(
#     'https://cdn.jsdelivr.net/gh/bangumi-data/bangumi-data/dist/data.json'
# ).json()
with (base_dir / '..' / 'bangumi-data' / 'dist' /
      'data.json').open('r', encoding='utf-8') as f:
    data = json.load(f)


def save_bangumi_data_to_db():
    for item in tqdm.tqdm(data['items']):
        d = {'title': item['titleTranslate'].get('zh-Hans', None)}
        if not d['title']:
            d['title'] = item['title']
        else:
            d['title'] = d['title'][0]
        for site in item['sites']:
            if site['site'] in ['bilibili', 'iqiyi']:
                d['bangumi_id'] = site.get('id', None)
                d['website'] = site['site']
            else:
                continue
            site_bangumi = [
                site for site in item['sites'] if site['site'] == 'bangumi'
            ]
            if site_bangumi:
                site_bangumi = site_bangumi[0]
            else:
                continue
            if site_bangumi.get('id', None):
                d['subject_id'] = site_bangumi.get('id', None)
                if d.get('bangumi_id'):
                    BangumiSource.replace(
                        bangumi_id=d['bangumi_id'],
                        source=d['website'],
                        subject_id=d['subject_id'],
                    ).execute()


def save_patch_to_db():

    with open(base_dir / 'patch.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in tqdm.tqdm(data):
        # for item in items:
        website = item['website']
        if item.get('subject_id'):
            subject_id = item['subject_id']
        elif item.get('subjectID'):
            subject_id = item['subjectID']
        else:
            subject_id = item['subject'].split('/')[-1]
        if item.get('bangumi_id'):
            bangumi_id = item['bangumi_id']
        elif item.get('bangumiID'):
            bangumi_id = item['bangumiID']
        else:
            raise ValueError('item has no bangumi id')

        BangumiSource.insert(
            bangumi_id=bangumi_id,
            source=website,
            subject_id=subject_id,
        ).on_conflict_replace('REPLACE',
                              preserve=(BangumiSource.subject_id, )).execute()
        MissingBangumi.delete().where(
            MissingBangumi.source == website,
            MissingBangumi.bangumi_id == bangumi_id,
        ).execute()


if __name__ == '__main__':
    with database.db.allow_sync():
        # BangumiSource.create_table()
        # MissingBangumi.create_table()
        save_bangumi_data_to_db()
        # save_patch_to_db()