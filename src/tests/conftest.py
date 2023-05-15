import pytest


@pytest.fixture(autouse=True, scope="session")
def test_fixture():
    """This is a test fixture function.
    Since the scope is session, this function will be called only once for the entire test session
    and the fixture will be shared with all the test functions.
    Scopes in pytest fixtures define the lifetime and visibility of fixture instances.

    Function Scope: This is the default scope for fixtures.
    A fixture with function scope is created and destroyed for each test function that uses it.
    It ensures that each test function gets a fresh instance of the fixture.

    Class Scope: A fixture with class scope is created and destroyed once for each test class that uses it.
    All test methods within the class share the same fixture instance.
    This scope is useful when you need to set up expensive resources that can be shared across multiple test methods.

    Module Scope: A fixture with module scope is created and destroyed once for each module (Python file) that uses it.
    All test functions within the module share the same fixture instance.
    This scope is useful when you have multiple test functions that require a common setup.

    Session Scope: A fixture with session scope is created and destroyed once for the entire test session.
    The session scope is especially useful when you have expensive resources that can be shared across multiple test
    modules.

    You can have multiple test fixtures in a test module with different scopes, and they will be called accordingly.
    """

    # This is when the tests start running (setup)

    yield

    # This is when the tests end running (teardown)
