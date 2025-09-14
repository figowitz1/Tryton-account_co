# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from sql import Table
from decimal import Decimal

from trytond.i18n import gettext
from trytond.model import ModelView, fields
from trytond.pool import PoolMeta, Pool


class AccountTemplate(metaclass=PoolMeta):
    __name__ = 'account.account.template'
    party_required = fields.Boolean('Party Required')

    @classmethod
    def __setup__(cls):
        super(AccountTemplate, cls).__setup__()
        cls.party_required.domain = []


class Account(metaclass=PoolMeta):
    __name__ = 'account.account'
    party_required = fields.Boolean('Party Required')

    @classmethod
    def __setup__(cls):
        super(Account, cls).__setup__()
        cls.party_required.domain = []
