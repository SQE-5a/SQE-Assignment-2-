# SQE-Assignment-2-
This assignment of Software Quality Assurance Course is related to Automation of testing


Existing Testing automation testcases observations and understandings:-



API existing test cases automation observations(By:Jawad Haider):

->Language used for api test cases automation by magento website luma is php.They have done their most of api test cases automation in php.
->They have done api testing automation for Controller, Model, Exception.
->There are different api testings done by them like authorization,Config,Plugin,Rest,Soap,_files( reference is:   https://github.com/magento/magento2/tree/2.4-develop/app/code/Magento/Webapi/Test/Unit)
->They have done api testing of all in the way that they check for correct scenario and also false scenario using function assertEquals($expectedOutputDataArray, $outputData)
->They have used get functions in the beginning of api testing. 
->They give variables in which data comes dynamically when api is used.
->Then they compare their values with the expected outcomes or expected values ,and assert gives error when scenario false or expected outcome not appear and vice versa.


