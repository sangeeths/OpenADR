from openadr import config as oadrCfg

from openadr.services.EiAvail.manager         import Response as EiAvailResponse
from openadr.services.EiEnroll.manager        import Response as EiEnrollResponse
from openadr.services.EiEvent.EiEventManager  import Response as EiEventResponse
from openadr.services.EiMarketContext.manager import Response as EiMarketContextResponse
from openadr.services.EiOpt.manager           import Response as EiOptResponse
from openadr.services.EiQuote.manager         import Response as EiQuoteResponse
from openadr.services.EiRegisterParty.manager import Response as EiRegisterPartyResponse
from openadr.services.EiReport.manager        import Response as EiReportResponse

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


