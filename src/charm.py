#!/usr/bin/env python3
# Copyright 2022 Billy Olsen
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Refer to the following post for a quick-start guide that will help you
develop a new k8s charm using the Operator Framework:

    https://discourse.charmhub.io/t/4208
"""

import logging

from ops.charm import CharmBase
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus

from charms.operator_libs_linux.v1 import snap

logger = logging.getLogger(__name__)


class CharmDiscoveryserverCharm(CharmBase):
    """Charm the service."""

    _stored = StoredState()

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.install, self._on_install)

    def _on_install(self, event):
        """Installs the discoveryserver snap

        :param event: install event
        :type event: ops.framework.EventBase
        :return: None
        """
        try:
            discovery_server = snap.add(
                snap_names='discoveryserver',
                channel='latest/edge',
            )
            logger.debug('Successfully install discoveryserver')
        except snap.SnapError as e:
            logger.exception('Error occurred installing discoveryserver snap.')
            raise
        # Learn more about statuses in the SDK docs:
        # https://juju.is/docs/sdk/constructs#heading--statuses
        self.unit.status = ActiveStatus()



if __name__ == "__main__":
    main(CharmDiscoveryserverCharm)
