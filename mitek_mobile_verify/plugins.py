# -*- coding: utf-8 -*-

from zeep import Plugin
from lxml import etree
import logging

__author__ = 'lundberg'

logger = logging.getLogger(__name__)


class DoctorPlugin(Plugin):

    def ingress(self, envelope, http_headers, operation):

        # Remove Security element from response (it is unhandled)
        # TODO: Check if it's a zeep bug or wsdl/xsd missmatch
        prefixmap = {'o': 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd'}
        for elem in envelope.xpath('///o:Security', namespaces=prefixmap):
            logger.info('Removed Security element from envelope header:')
            logger.info('{}'.format(etree.tostring(elem, pretty_print=True)))
            elem.getparent().remove(elem)

        return envelope, http_headers
