# laod steps
from behave import given, when, then
from service import service


@given('the service is running')
def step_impl(context):
    context.service = service.Service()
    context.service.start() # start the service


@when('the service is stopped')
def step_impl(context):
    context.service.stop()


@then('the service is stopped')
def step_impl(context):
    assert context.service.is_stopped() == True
```

### 4. Run the tests
    
    ```bash

    $ behave

    ```

### 5. Output
    
    ```bash

        