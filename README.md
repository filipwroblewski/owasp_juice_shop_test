# owasp_juice_shop_test

## Using localhost

```
├───test_localhost.py
└───chromedriver
    └───chromedriver.exe
```

chromedriver.exe version for Chrome 119.0.6045.x

Faild
```
F                                                                                       
======================================================================                  
FAIL: test_juice_shop_title (__main__.JuiceShopTest.test_juice_shop_title)              
----------------------------------------------------------------------                  
Traceback (most recent call last):                                                      
  File "c:\Codding\docker\owasp_juice_shop_test\test_v1.py", line 29, in test_juice_shop
_title                                                                                  
    self.assertIn(expected_title, self.driver.title)                                    
AssertionError: 'OWASP Juice Shope' not found in 'OWASP Juice Shop'                     
                                                                                        
----------------------------------------------------------------------                  
Ran 1 test in 4.639s                                                                    
                                                                                        
FAILED (failures=1)                                                                     
                                                                                        
```

Success
```
.
----------------------------------------------------------------------
Ran 1 test in 8.545s

OK

```


## Using Docker

```
├───docker-compose.yml
├───Dockerfile
└───test.py
```

Testing results can be viewd (using Selenium Grid) on `http://127.0.0.1:4444/` or `http://localhost:4444/` when docker images are up.