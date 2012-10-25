# -*- coding: utf-8 -*-
#
# Copyright © 2012 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.

from katello.client.api.base import KatelloAPI
from katello.client.utils.encoding import u_str

class OrganizationSystemInfoKeysAPI(KatelloAPI):
    """
    Connection class to access default system info keys under an organization
    """
    def create(self, org_name, keyname):
        data = {'keyname': keyname}
        path = "/api/organizations/%s/system_info_keys" % u_str(org_name)
        return self.server.POST(path, data)[1]

    def index(self, org_name):
        path = "/api/organizations/%s/system_info_keys" % u_str(org_name)
        return self.server.GET(path)[1]

    def destroy(self, org_name, keyname):
        path = "/api/organizations/%s/system_info_keys/%s" % (u_str(org_name), u_str(keyname))
        return self.server.DELETE(path)[1]

    def apply(self, org_name):
        path = "/api/organizations/%s/system_info_keys/apply" % u_str(org_name)
        return self.server.GET(path)[1]
