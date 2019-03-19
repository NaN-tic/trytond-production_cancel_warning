# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import ModelView, Workflow
from trytond.pool import PoolMeta

__all__ = ['Production']


class Production:
    __name__ = 'production'
    __metaclass__ = PoolMeta

    @classmethod
    def __setup__(cls):
        super(Production, cls).__setup__()
        cls._error_messages.update({
                'are_you_sure': ('Production "%(production)s" will '
                    'be cancelled, are you sure you want to continue?')
                })

    @classmethod
    @ModelView.button
    @Workflow.transition('cancel')
    def cancel(cls, productions):
        for production in productions:
            cls.raise_user_warning('are_you_sure_%d' % production.id,
                'are_you_sure', {
                    'production': production.code,
                })
        super(Production, cls).cancel(productions)
