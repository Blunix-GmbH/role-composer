import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

COMPOSER_VERSION = '1.6.5'


def test_composer(host):
    cmd = host.run('composer')

    assert cmd.rc == 0

    hits = 0
    for line in cmd.stdout.splitlines():
        if line.strip().startswith(
                'Composer version {}'.format(COMPOSER_VERSION)):
            hits += 1
    assert hits == 1
