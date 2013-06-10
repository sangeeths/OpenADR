from openadr import config as oadrCfg

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
OADR_MESSAGE_HANDLER = {oadrCfg.OADR_SERVICE.EiAvail         : EiAvailResponse ,
                        oadrCfg.OADR_SERVICE.EiEnroll        : EiEnrollResponse,
                        oadrCfg.OADR_SERVICE.EiEvent         : EiEventResponse,
                        oadrCfg.OADR_SERVICE.EiMarketContext : EiMarketContextResponse,
                        oadrCfg.OADR_SERVICE.EiOpt           : EiOptResponse,
                        oadrCfg.OADR_SERVICE.EiQuote         : EiQuoteResponse,
                        oadrCfg.OADR_SERVICE.EiRegisterParty : EiRegisterPartyResponse,
                        oadrCfg.OADR_SERVICE.EiReport        : EiReportResponse
                       }


