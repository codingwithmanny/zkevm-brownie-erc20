#!/usr/bin/python3

from brownie import Token, accounts

def main():
    accounts.load('<REPLACE-WITH-YOUR-BROWNIE-ACCOUNT-ID>')
    return Token.deploy("zkEVM Test Token", "ZKTST", 18, 1e21, {'from': accounts[0]})
