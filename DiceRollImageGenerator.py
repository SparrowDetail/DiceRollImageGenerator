from PIL import Image, ImageDraw, ImageFont

DIE_COORDINATES = [(10, 54), (116, 54), (222, 54), (328, 54)]
IMAGE_HEADER_Y_COORDINATE = 5
IMAGE_FOOTER_Y_COORDINATE = 160
RGB_FONT_COLOR = (255, 255, 255)

ASSET_LIBRARY_DIRECTORY = "./Assets/"
BASE_IMAGE_DIMENSIONS = (434, 204)

IMAGE_TEXT_FONT = ImageFont.truetype("./Fonts/Mitr/Mitr-Regular.ttf", 32)

def generateDieImage(rollValues: list, dieType: int) -> Image:
    """
    Generates and returns a formatted 434 by 204 px image displaying dice roll values and their
    total sum. Recommended to access this function using the defined die generation functions
    (i.e. generateD6Image) to help prevent raising a RollValueAndTypeError. The passed die type
    must represent a valid DnD die maximum value ([2, 4, 6, 8, 10, 12, 20]). If an asset is missing or
    formatted incorrectly (e.g. D6_1.png) a FileNotFoundError will be raised.

    :param rollValues: list containing one to four int values within expected range of 1 to dieType.
    :param dieType: int value representing a typical DnD die type ([2, 4, 6, 8, 10, 12, 20]).
    :return: generated 434 by 204 px image containing die rolls and calculated total.
    :raise RollValueAndTypeError: where dieType is invalid or passed list does not meet requirements.
    :raise FileNotFoundError: when asset cannot be found, must be named appropriately and located in the Asset directory (e.g. file path: "./Assets/D6_1.png")
    """
    CheckError = RollValueAndTypeError(rollValues, dieType)
    if CheckError.valid:
        baseImage = Image.new(mode="RGBA", size=BASE_IMAGE_DIMENSIONS)
        rollCounter = 0
        rollTypeHeaderText = f"Roll {CheckError.listSize}D{dieType}"
        rollTotalFooterText = f"Total: {sum(rollValues)}"

        for i in rollValues:
            dieImage = Image.open(ASSET_LIBRARY_DIRECTORY + f"D{dieType}_{i}.png")

            baseImage.paste(dieImage, DIE_COORDINATES[rollCounter])
            rollCounter += 1

            dieImage.close()
        
        textGraphicCreator = ImageDraw.Draw(baseImage)
        centerHeaderXCoordinate = (BASE_IMAGE_DIMENSIONS[0] - textGraphicCreator.textbbox((0,0),text=rollTypeHeaderText,font=IMAGE_TEXT_FONT)[2]) / 2
        centerFooterXCoordinate = (BASE_IMAGE_DIMENSIONS[0] - textGraphicCreator.textbbox((0,0),text=rollTotalFooterText,font=IMAGE_TEXT_FONT)[2]) / 2
        textGraphicCreator.text((centerHeaderXCoordinate, IMAGE_HEADER_Y_COORDINATE), rollTypeHeaderText, font=IMAGE_TEXT_FONT, fill=RGB_FONT_COLOR)
        textGraphicCreator.text((centerFooterXCoordinate, IMAGE_FOOTER_Y_COORDINATE), rollTotalFooterText, font=IMAGE_TEXT_FONT, fill=RGB_FONT_COLOR)
        
        return baseImage
    else:
        raise CheckError

def generateD2Image(rollValues: list) -> Image:
    """
    Generates and returns a formatted 434 by 204 px image displaying dice roll values
    and their total sum. Roll values should be passed in the form of an integer list of
    size 1 to 4. The integers must also represent dice rolls within the range present on
    a traditional two sided die/coin (1-2).

    :param rollValues: list containing one to four int values within expected range of 1-2.
    :return: generated image representing die rolls.
    :raise RollValueAndTypeError: where list expectations are not met 
    :raise FileNotFoundError: where assets are missing or formatted incorrectly (e.g. file path: "./Assets/D2_1.png")
    """
    return generateDieImage(rollValues, 2)

def generateD4Image(rollValues: list) -> Image:
    """
    Generates and returns a formatted 434 by 204 px image displaying dice roll values
    and their total sum. Roll values should be passed in the form of an integer list of
    size 1 to 4. The integers must also represent dice rolls within the range present on
    a traditional four sided die (1-4).

    :param rollValues: list containing one to four int values within expected range of 1-4.
    :return: generated image representing die rolls.
    :raise RollValueAndTypeError: where list expectations are not met 
    :raise FileNotFoundError: where assets are missing or formatted incorrectly (e.g. file path: "./Assets/D4_1.png")
    """
    return generateDieImage(rollValues, 4)

def generateD6Image(rollValues: list) -> Image:
    """
    Generates and returns a formatted 434 by 204 px image displaying dice roll values
    and their total sum. Roll values should be passed in the form of an integer list of
    size 1 to 4. The integers must also represent dice rolls within the range present on
    a traditional six sided die (1-6).

    :param rollValues: list containing one to four int values within expected range of 1-6.
    :return: generated image representing die rolls.
    :raise RollValueAndTypeError: where list expectations are not met 
    :raise FileNotFoundError: where assets are missing or formatted incorrectly (e.g. file path: "./Assets/D6_1.png")
    """
    return generateDieImage(rollValues, 6)

def generateD8Image(rollValues: list) -> Image:
    """
    Generates and returns a formatted 434 by 204 px image displaying dice roll values
    and their total sum. Roll values should be passed in the form of an integer list of
    size 1 to 4. The integers must also represent dice rolls within the range present on
    a traditional eight sided die (1-8).

    :param rollValues: list containing one to four int values within expected range of 1-8.
    :return: generated image representing die rolls.
    :raise RollValueAndTypeError: where list expectations are not met 
    :raise FileNotFoundError: where assets are missing or formatted incorrectly (e.g. file path: "./Assets/D8_1.png")
    """
    return generateDieImage(rollValues, 8)

def generateD10Image(rollValues: list) -> Image:
    """
    Generates and returns a formatted 434 by 204 px image displaying dice roll values
    and their total sum. Roll values should be passed in the form of an integer list of
    size 1 to 4. The integers must also represent dice rolls within the range present on
    a traditional ten sided die (1-10).

    :param rollValues: list containing one to four int values within expected range of 1-10.
    :return: generated image representing die rolls.
    :raise RollValueAndTypeError: where list expectations are not met 
    :raise FileNotFoundError: where assets are missing or formatted incorrectly (e.g. file path: "./Assets/D10_1.png")
    """
    return generateDieImage(rollValues, 10)

def generateD12Image(rollValues: list) -> Image:
    """
    Generates and returns a formatted 434 by 204 px image displaying dice roll values
    and their total sum. Roll values should be passed in the form of an integer list of
    size 1 to 4. The integers must also represent dice rolls within the range present on
    a traditional twelve sided die (1-12).

    :param rollValues: list containing one to four int values within expected range of 1-12.
    :return: generated image representing die rolls.
    :raise RollValueAndTypeError: where list expectations are not met 
    :raise FileNotFoundError: where assets are missing or formatted incorrectly (e.g. file path: "./Assets/D12_1.png")
    """
    return generateDieImage(rollValues, 12)

def generateD20Image(rollValues: list) -> Image:
    """
    Generates and returns a formatted 434 by 204 px image displaying dice roll values
    and their total sum. Roll values should be passed in the form of an integer list of
    size 1 to 4. The integers must also represent dice rolls within the range present on
    a traditional twenty sided die (1-20).

    :param rollValues: list containing one to four int values within expected range of 1-20.
    :return: generated image representing die rolls.
    :raise RollValueAndTypeError: where list expectations are not met 
    :raise FileNotFoundError: where assets are missing or formatted incorrectly (e.g. file path: "./Assets/D20_1.png")
    """
    return generateDieImage(rollValues, 20)

class RollValueAndTypeError(Exception):
    """
    Error class used to validate key image generation factors. A RollValueAndTypeError is raised when the passed list exceeds
    four elements, does not contain only int values, or exceeds the defined max roll value. This simplifies the validation process
    for image generation parameters and provides meaningful error messages for debugging purposes.

    :inherit Exception:
    :param rollList: Passed list to be validated
    :param maxRoll: Expected maximum int value stored in the passed list
    """
    valid:bool
    listSize:int
    maxExpectedRollValue:int
    __isIntList__:bool = True
    __isInRollMaxRange__:bool = True
    __isAcceptedDieType__:bool = True
    __acceptedDieTypes__:list = [2, 4, 6, 8, 10, 12, 20]

    def __init__(self, rollList: list, maxRoll:int, *args: object) -> None:
        super().__init__(self, *args)
        self.listSize = len(rollList)
        self.maxExpectedRollValue = maxRoll
        self.valid = self.__isValidList__(rollList, maxRoll)

    def __str__(self) -> str:
        if not self.__isAcceptedDieType__:
            return f"Invalid die type passed: D{self.maxExpectedRollValue}"
        elif not self.__isIntList__:
            return f"The list must contain only one to four int values: list size ({self.listSize})"
        elif not self.__isInRollMaxRange__:
            return f"A list element is outside the expected max roll value: {self.maxExpectedRollValue}"
        return super().__str__()
    
    def __isValidList__(self, list:list, dieMaxRoll:int) -> bool:
        """
        Verifies the target list meets the expectations of the calling function. The
        list should contain 1 to 4 elements of type int with a value from one to a 
        specified maximum value.

        :param list: the target list being validated.
        :param dieMaxRoll: maximum int value expected within the list. Range 1 to dieMaxRoll (inclusive).
        :return: a boolean value
        """
        if dieMaxRoll in self.__acceptedDieTypes__:
            if (len(list) <= 4 and all(isinstance(i,int) for i in list)):
                for i in list:
                    if i < 1 or i > dieMaxRoll:
                        self.__isInRollMaxRange__ = False
                        return False
                return True
            else:
                self.__isIntList__ = False
                return False
        else:
            self.__isAcceptedDieType__ = False
            return False