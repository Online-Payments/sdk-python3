# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject


class BrowserData(DataObject):
    """
    | Object containing information regarding the browser of the customer
    """

    __color_depth = None
    __java_enabled = None
    __java_script_enabled = None
    __screen_height = None
    __screen_width = None

    @property
    def color_depth(self) -> int:
        """
        | ColorDepth in bits. Value is returned from the screen.colorDepth property.
        
        | If you use the latest version of our JavaScript Client SDK, we will collect this data and include it in the encryptedCustomerInput property. We will then automatically populate this data if available.
        
        | Note: This data can only be collected if JavaScript is enabled in the browser. This means that 3-D Secure version 2.1 requires the use of JavaScript to enabled. In the upcoming version 2.2 of the specification this is no longer a requirement.

        Type: int
        """
        return self.__color_depth

    @color_depth.setter
    def color_depth(self, value: int):
        self.__color_depth = value

    @property
    def java_enabled(self) -> bool:
        """
        | true =Java is enabled in the browser
        
        | false = Java is not enabled in the browser
        
        | Value is returned from the navigator.javaEnabled property.
        
        | If you use the latest version of our JavaScript Client SDK, we will collect this data and include it in the encryptedCustomerInput property. We will then automatically populate this data if available.
        
        | Note: This data can only be collected if JavaScript is enabled in the browser. This means that 3-D Secure version 2.1 requires the use of JavaScript to enabled. In the upcoming version 2.2 of the specification this is no longer a requirement.

        Type: bool
        """
        return self.__java_enabled

    @java_enabled.setter
    def java_enabled(self, value: bool):
        self.__java_enabled = value

    @property
    def java_script_enabled(self) -> bool:
        """
        | * true = JavaScript is enabled in the browser.
        | * false = JavaScript is not enabled in the browser. In this case the following parameters are not mandatory anymore: colorDepth, javaEnabled, screenHeight, screenWidth, timezoneOffsetUtcMinutes.

        Type: bool
        """
        return self.__java_script_enabled

    @java_script_enabled.setter
    def java_script_enabled(self, value: bool):
        self.__java_script_enabled = value

    @property
    def screen_height(self) -> str:
        """
        | Height of the screen in pixels. Value is returned from the screen.height property.
        
        | If you use the latest version of our JavaScript Client SDK, we will collect this data and include it in the encryptedCustomerInput property. We will then automatically populate this data if available.
        
        | Note: This data can only be collected if JavaScript is enabled in the browser. This means that 3-D Secure version 2.1 requires the use of JavaScript to enabled. In the upcoming version 2.2 of the specification this is no longer a requirement.

        Type: str
        """
        return self.__screen_height

    @screen_height.setter
    def screen_height(self, value: str):
        self.__screen_height = value

    @property
    def screen_width(self) -> str:
        """
        | Width of the screen in pixels. Value is returned from the screen.width property.
        
        | If you use the latest version of our JavaScript Client SDK, we will collect this data and include it in the encryptedCustomerInput property. We will then automatically populate this data if available.
        
        | Note: This data can only be collected if JavaScript is enabled in the browser. This means that 3-D Secure version 2.1 requires the use of JavaScript to enabled. In the upcoming version 2.2 of the specification this is no longer a requirement.

        Type: str
        """
        return self.__screen_width

    @screen_width.setter
    def screen_width(self, value: str):
        self.__screen_width = value

    def to_dictionary(self):
        dictionary = super(BrowserData, self).to_dictionary()
        if self.color_depth is not None:
            dictionary['colorDepth'] = self.color_depth
        if self.java_enabled is not None:
            dictionary['javaEnabled'] = self.java_enabled
        if self.java_script_enabled is not None:
            dictionary['javaScriptEnabled'] = self.java_script_enabled
        if self.screen_height is not None:
            dictionary['screenHeight'] = self.screen_height
        if self.screen_width is not None:
            dictionary['screenWidth'] = self.screen_width
        return dictionary

    def from_dictionary(self, dictionary):
        super(BrowserData, self).from_dictionary(dictionary)
        if 'colorDepth' in dictionary:
            self.color_depth = dictionary['colorDepth']
        if 'javaEnabled' in dictionary:
            self.java_enabled = dictionary['javaEnabled']
        if 'javaScriptEnabled' in dictionary:
            self.java_script_enabled = dictionary['javaScriptEnabled']
        if 'screenHeight' in dictionary:
            self.screen_height = dictionary['screenHeight']
        if 'screenWidth' in dictionary:
            self.screen_width = dictionary['screenWidth']
        return self
