from typing import Dict, NamedTuple
from os import environ


DEPOSIT_CLI_VERSION = '1.2.0'


class BaseChainSetting(NamedTuple):
    ETH2_NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes



GNOSIS_TESTNET = 'gnosis-testnet'
GNOSIS = 'gnosis'
TEST = 'test'


# Gnosis Beacon Chain testnet setting
GnosisTestnetSetting = BaseChainSetting(ETH2_NETWORK_NAME=GNOSIS_TESTNET, GENESIS_FORK_VERSION=bytes.fromhex('00006464'))
# Gnosis Beacon Chain setting
GnosisSetting = BaseChainSetting(ETH2_NETWORK_NAME=GNOSIS, GENESIS_FORK_VERSION=bytes.fromhex('00000064'))
# Test Setting
TestSetting = BaseChainSetting(ETH2_NETWORK_NAME=TEST, GENESIS_FORK_VERSION=bytes.fromhex(environ.get('GENESIS_FORK_VERSION', '12345678')))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    GNOSIS_TESTNET: GnosisTestnetSetting,
    GNOSIS: GnosisSetting,
    TEST: TestSetting,
}


def get_chain_setting(chain_name: str = GNOSIS) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]
