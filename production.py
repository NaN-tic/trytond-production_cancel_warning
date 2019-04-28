# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, Workflow
from trytond.pool import PoolMeta
from trytond.i18n import gettext
from trytond.exceptions import UserWarning
from trytond.i18n import gettext
from trytond.exceptions import UserError

__all__ = ['Production']


class Production(metaclass=PoolMeta):
    __name__ = 'production'

    @classmethod
    @ModelView.button
    @Workflow.transition('cancel')
    def cancel(cls, productions):
        for production in productions:
            raise UserWarning('are_you_sure_%d' % production.id, gettext(
                    'production_cancel_warning.are_you_sure',
                    production=production.code))
        super(Production, cls).cancel(productions)
