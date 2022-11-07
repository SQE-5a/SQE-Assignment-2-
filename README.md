# SQE-Assignment-2-
This assignment of Software Quality Assurance Course is related to Automation of testing


 Observations and Understandings of Existing Testing (ui,api,unit)automation done by Magento :-


-------------------------------------------------------------------------------------------------------------------------------------------------------
OBSERVATIONS OF EXISTING API TESTING AUTOMATION done by magento (By:Jawad Haider):

->Language used for api test cases automation by magento website luma is php.They have done their most of api test cases automation in php.
->They have done api testing automation for Controller, Model, Exception.
->There are different api testings done by them like authorization,Config,Plugin,Rest,Soap,_files( reference is:   https://github.com/magento/magento2/tree/2.4-develop/app/code/Magento/Webapi/Test/Unit)
->They have done api testing of all in the way that they check for correct scenario and also false scenario using function assertEquals($expectedOutputDataArray, $outputData)
->They have used get functions in the beginning of api testing. 
->They give variables in which data comes dynamically when api is used.
->Then they compare their values with the expected outcomes or expected values ,and assert gives error when scenario false or expected outcome not appear and vice versa.

Selected one existing api test case automation demonstration with code references: 

To observe and demonstrate with code references,I have selected DataObjectProcessorTest.php from Model existing api test automation directory .Its link of code is :    https://github.com/magento/magento2/blob/2.4-develop/app/code/Magento/Webapi/Test/Unit/Model/DataObjectProcessorTest.php .Language used in that api test automation is php. 

Connections and setups are get and handeled in setup function.
Then comes testDataObjectProcessor() function which is very important for the api testing!
public function testDataObjectProcessor()
    {
        $objectManager =  new ObjectManager($this);
        /** @var TestDataObject $testDataObject */
        $testDataObject = $objectManager->getObject(TestDataObject::class);

        $expectedOutputDataArray = [
            'id' => '1',
            'address' => 'someAddress',
            'default_shipping' => 'true',
            'required_billing' => 'false',
        ];

        $testDataObjectType = TestDataInterface::class;
        $outputData = $this->dataObjectProcessor->buildOutputDataArray($testDataObject, $testDataObjectType);
        $this->assertEquals($expectedOutputDataArray, $outputData);
    }

In above function,parameters are will be handeled when new Object ObjectManager() created and getObject(parameters) functionnis called.
There is an array having values of the variables which are expected when get request of api will be called and actions are performed.
BuildOutputDataArray($testDataObject, $testDataObjectType) function will be called to get the values of variables of api actually occuring like 'id','address','default_shipping','required_billing' and these values will be saved in the outputData.

assertEquals($expectedOutputDataArray, $outputData) function is used to check whether api test true or false.
    ->If every variable value of outputData is equal to expectedOutputDataArray variables values then api test is true . 
    ->If any variable value of outputData is not equal to expectedOutputDataArray variables values then api test is false . 
    
-------------------------------------------------------------------------------------------------------------------------------------------------------

OBSERVATIONS OF EXISTING UI TESTING AUTOMATION done by magento (By:Muhammad Hashim):

-> The language used for UI Automation is Xml.
-> The have done UI autonmtion for the multiple components of the website.
-> They have use xml version 1.o for the testing.
-> For automation in this language multiple keywords are used such as annotation,description,antigroup,actiongroup.

Following is the link of one automation done in the website
   magento2/app/code/Magento/Ui/Test/Mftf/ActionGroup/AdminGridAssertTotalPageCountActionGroup.xml


Following is the code:

<actionGroups xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="urn:magento:mftf:Test/etc/actionGroupSchema.xsd">
    <actionGroup name="AdminGridAssertTotalPageCountActionGroup">
        <annotations>
            <description>
                Assert total page count on admin grid
            </description>
        </annotations>
        <arguments>
            <argument name="expectedTotalPageCount" defaultValue="1" type="string"/>
        </arguments>

        <waitForElementVisible selector="{{AdminDataGridPaginationSection.totalPagesCount('expectedTotalPageCount')}}" stepKey="waitForTotalPagesCountToBeVisible"/>
    </actionGroup>
</actionGroups>


-> First they use the actiongroup in which link is stored.It is done for reusability purposes.
-> Here is annotation also used, its sole purpose is to specify schema components.
-> An argument is what you pass into a function (also known as a subroutine). Arguments are also known as parameters. A function might take an argument and use it      to calculate something or modify the argument itself.
-> .waitForElementVisible () Suggest edits Waits a given time in milliseconds (default 5000ms) for an element to be visible in the page before performing any other commands or assertions. If the element fails to be present and visible in the specified amount of time, the test fails.


--------------------------------------------------------------------------------------------------------------------------------------------------



