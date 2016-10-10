# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2016  Kaltura Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
# @ignore
# ===================================================================================================
# @package Kaltura
# @subpackage Client
from Core import *
from ContentDistribution import *
from ..Base import *

########## enums ##########
# @package Kaltura
# @subpackage Client
class KalturaUverseClickToOrderDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaUverseClickToOrderDistributionProviderOrderBy(object):

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaUverseClickToOrderDistributionProvider(KalturaDistributionProvider):
    def __init__(self,
            type=NotImplemented,
            name=NotImplemented,
            scheduleUpdateEnabled=NotImplemented,
            availabilityUpdateEnabled=NotImplemented,
            deleteInsteadUpdate=NotImplemented,
            intervalBeforeSunrise=NotImplemented,
            intervalBeforeSunset=NotImplemented,
            updateRequiredEntryFields=NotImplemented,
            updateRequiredMetadataXPaths=NotImplemented):
        KalturaDistributionProvider.__init__(self,
            type,
            name,
            scheduleUpdateEnabled,
            availabilityUpdateEnabled,
            deleteInsteadUpdate,
            intervalBeforeSunrise,
            intervalBeforeSunset,
            updateRequiredEntryFields,
            updateRequiredMetadataXPaths)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDistributionProvider.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUverseClickToOrderDistributionProvider.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProvider.toParams(self)
        kparams.put("objectType", "KalturaUverseClickToOrderDistributionProvider")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaUverseClickToOrderDistributionProfile(KalturaConfigurableDistributionProfile):
    def __init__(self,
            id=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            partnerId=NotImplemented,
            providerType=NotImplemented,
            name=NotImplemented,
            status=NotImplemented,
            submitEnabled=NotImplemented,
            updateEnabled=NotImplemented,
            deleteEnabled=NotImplemented,
            reportEnabled=NotImplemented,
            autoCreateFlavors=NotImplemented,
            autoCreateThumb=NotImplemented,
            optionalFlavorParamsIds=NotImplemented,
            requiredFlavorParamsIds=NotImplemented,
            optionalThumbDimensions=NotImplemented,
            requiredThumbDimensions=NotImplemented,
            optionalAssetDistributionRules=NotImplemented,
            requiredAssetDistributionRules=NotImplemented,
            sunriseDefaultOffset=NotImplemented,
            sunsetDefaultOffset=NotImplemented,
            recommendedStorageProfileForDownload=NotImplemented,
            recommendedDcForDownload=NotImplemented,
            recommendedDcForExecute=NotImplemented,
            fieldConfigArray=NotImplemented,
            itemXpathsToExtend=NotImplemented,
            useCategoryEntries=NotImplemented,
            feedUrl=NotImplemented,
            backgroundImageWide=NotImplemented,
            backgroundImageStandard=NotImplemented):
        KalturaConfigurableDistributionProfile.__init__(self,
            id,
            createdAt,
            updatedAt,
            partnerId,
            providerType,
            name,
            status,
            submitEnabled,
            updateEnabled,
            deleteEnabled,
            reportEnabled,
            autoCreateFlavors,
            autoCreateThumb,
            optionalFlavorParamsIds,
            requiredFlavorParamsIds,
            optionalThumbDimensions,
            requiredThumbDimensions,
            optionalAssetDistributionRules,
            requiredAssetDistributionRules,
            sunriseDefaultOffset,
            sunsetDefaultOffset,
            recommendedStorageProfileForDownload,
            recommendedDcForDownload,
            recommendedDcForExecute,
            fieldConfigArray,
            itemXpathsToExtend,
            useCategoryEntries)

        # @var string
        # @readonly
        self.feedUrl = feedUrl

        # @var string
        self.backgroundImageWide = backgroundImageWide

        # @var string
        self.backgroundImageStandard = backgroundImageStandard


    PROPERTY_LOADERS = {
        'feedUrl': getXmlNodeText, 
        'backgroundImageWide': getXmlNodeText, 
        'backgroundImageStandard': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUverseClickToOrderDistributionProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfile.toParams(self)
        kparams.put("objectType", "KalturaUverseClickToOrderDistributionProfile")
        kparams.addStringIfDefined("backgroundImageWide", self.backgroundImageWide)
        kparams.addStringIfDefined("backgroundImageStandard", self.backgroundImageStandard)
        return kparams

    def getFeedUrl(self):
        return self.feedUrl

    def getBackgroundImageWide(self):
        return self.backgroundImageWide

    def setBackgroundImageWide(self, newBackgroundImageWide):
        self.backgroundImageWide = newBackgroundImageWide

    def getBackgroundImageStandard(self):
        return self.backgroundImageStandard

    def setBackgroundImageStandard(self, newBackgroundImageStandard):
        self.backgroundImageStandard = newBackgroundImageStandard


# @package Kaltura
# @subpackage Client
class KalturaUverseClickToOrderDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented):
        KalturaDistributionProviderFilter.__init__(self,
            orderBy,
            advancedSearch,
            typeEqual,
            typeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDistributionProviderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUverseClickToOrderDistributionProviderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDistributionProviderFilter.toParams(self)
        kparams.put("objectType", "KalturaUverseClickToOrderDistributionProviderBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaUverseClickToOrderDistributionProviderFilter(KalturaUverseClickToOrderDistributionProviderBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented):
        KalturaUverseClickToOrderDistributionProviderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            typeEqual,
            typeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUverseClickToOrderDistributionProviderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUverseClickToOrderDistributionProviderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUverseClickToOrderDistributionProviderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUverseClickToOrderDistributionProviderFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaUverseClickToOrderDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaConfigurableDistributionProfileFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaConfigurableDistributionProfileFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUverseClickToOrderDistributionProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfigurableDistributionProfileFilter.toParams(self)
        kparams.put("objectType", "KalturaUverseClickToOrderDistributionProfileBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaUverseClickToOrderDistributionProfileFilter(KalturaUverseClickToOrderDistributionProfileBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented):
        KalturaUverseClickToOrderDistributionProfileBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUverseClickToOrderDistributionProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUverseClickToOrderDistributionProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUverseClickToOrderDistributionProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUverseClickToOrderDistributionProfileFilter")
        return kparams


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaUverseClickToOrderService(KalturaServiceBase):
    """Uverse Click To Order Service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def getFeed(self, distributionProfileId, hash):
        kparams = KalturaParams()
        kparams.addIntIfDefined("distributionProfileId", distributionProfileId);
        kparams.addStringIfDefined("hash", hash)
        self.client.queueServiceActionCall('uverseclicktoorderdistribution_uverseclicktoorder', 'getFeed', None ,kparams)
        return self.client.getServeUrl()

########## main ##########
class KalturaUverseClickToOrderDistributionClientPlugin(KalturaClientPlugin):
    # KalturaUverseClickToOrderDistributionClientPlugin
    instance = None

    # @return KalturaUverseClickToOrderDistributionClientPlugin
    @staticmethod
    def get():
        if KalturaUverseClickToOrderDistributionClientPlugin.instance == None:
            KalturaUverseClickToOrderDistributionClientPlugin.instance = KalturaUverseClickToOrderDistributionClientPlugin()
        return KalturaUverseClickToOrderDistributionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'uverseClickToOrder': KalturaUverseClickToOrderService,
        }

    def getEnums(self):
        return {
            'KalturaUverseClickToOrderDistributionProfileOrderBy': KalturaUverseClickToOrderDistributionProfileOrderBy,
            'KalturaUverseClickToOrderDistributionProviderOrderBy': KalturaUverseClickToOrderDistributionProviderOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaUverseClickToOrderDistributionProvider': KalturaUverseClickToOrderDistributionProvider,
            'KalturaUverseClickToOrderDistributionProfile': KalturaUverseClickToOrderDistributionProfile,
            'KalturaUverseClickToOrderDistributionProviderBaseFilter': KalturaUverseClickToOrderDistributionProviderBaseFilter,
            'KalturaUverseClickToOrderDistributionProviderFilter': KalturaUverseClickToOrderDistributionProviderFilter,
            'KalturaUverseClickToOrderDistributionProfileBaseFilter': KalturaUverseClickToOrderDistributionProfileBaseFilter,
            'KalturaUverseClickToOrderDistributionProfileFilter': KalturaUverseClickToOrderDistributionProfileFilter,
        }

    # @return string
    def getName(self):
        return 'uverseClickToOrderDistribution'

