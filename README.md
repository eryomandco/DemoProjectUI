# DemoProjectUI
### **Demo project for automation testing of an online store "https://bravo31.ru/"**
This project uses **Python + POM + Selenium + Pytest + Allure** technologies.

### **Project structure:**
* **Base** - the basic methods that are used in tests. Based on this Class are built other Class-pages of online store.
* **Logs** - files with log records are placed here.
* **Pages** are classes of store pages that include locators, search methods for elements, methods with test steps.
* **Screenshots** - contains screenshots used to confirm some of test steps.
* **Test_results** - allure reports are placed here. You can use your own directory when running tests.
* **Tests** - here are the test files.
* **Utilities** - a file for recording logs is located here.
* File **conftest.py** contains fixtues that can be used to change the logic of tests.
* File **requirements.txt** contains libraries that need to be installed to run tests.

### **The logic of the tests.**
**test_authorizations.py** - includes three tests:
1. Authorization test with correct test data.
2. Authorization test with an incorrect login.
3. Authorization test with an incorrect password.

Priority of launch these tests was changed

**test_full_path_product.py** - includes a full business path test. Authorization, going to the Perfume page, going to the For Men page, using pre-filtering in the catalog, going to the Product page, adding the product to the Cart, going to the Place Order page, filling in the city field and deleting the product.

All tests used verification methods - url compliance with expected, header compliance with expected, screenshots as confirmation.

### **You can run tests in PyCharm terminal using the command:**
> python3 -m pytest --alluredir=test_results/

OR

> python -m pytest --alluredir=test_results/

test_results/ is the folder where allure reports are included. You may use your own directory

### **To run the tests you need to install packages with the command:**
> pip install -r requirements.txt

NOTICE:
Your version of allure-pytest may be different
