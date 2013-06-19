from openadr import sysconfig as sysCfg

from openadr.services.EiAvail.EiAvailManager                 import Response as EiAvailResponse
from openadr.services.EiEnroll.EiEnrollManager               import Response as EiEnrollResponse
from openadr.services.EiEvent.EiEventManager                 import Response as EiEventResponse
from openadr.services.EiMarketContext.EiMarketContextManager import Response as EiMarketContextResponse
from openadr.services.EiOpt.EiOptManager                     import Response as EiOptResponse
from openadr.services.EiQuote.EiQuoteManager                 import Response as EiQuoteResponse
from openadr.services.EiRegisterParty.EiRegisterPartyManager import Response as EiRegisterPartyResponse
from openadr.services.EiReport.EiReportManager               import Response as EiReportResponse

#
# Response function handlers for all OADR_MESSAGE
#
OADR_MESSAGE_HANDLER = {
    sysCfg.OADR_SERVICE.EiAvail         : EiAvailResponse ,
    sysCfg.OADR_SERVICE.EiEnroll        : EiEnrollResponse,
    sysCfg.OADR_SERVICE.EiEvent         : EiEventResponse,
    sysCfg.OADR_SERVICE.EiMarketContext : EiMarketContextResponse,
    sysCfg.OADR_SERVICE.EiOpt           : EiOptResponse,
    sysCfg.OADR_SERVICE.EiQuote         : EiQuoteResponse,
    sysCfg.OADR_SERVICE.EiRegisterParty : EiRegisterPartyResponse,
    sysCfg.OADR_SERVICE.EiReport        : EiReportResponse
}


