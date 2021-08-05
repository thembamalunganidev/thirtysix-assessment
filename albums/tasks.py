from huey import crontab
from huey.contrib.djhuey import periodic_task

from albums.services import DiscogsSyncService
from thirtysix_assessment.config import Config

sync_service = DiscogsSyncService()


@periodic_task(crontab(minute='*/1'))
def sync_discogs_data():
    params = Config.DISCOGS_SYNC_FILTER_PARAMS
    sync_service.perform_sync(params)
