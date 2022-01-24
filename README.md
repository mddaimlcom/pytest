# end-presentation-

0. What are the goals and agenda of the presentation
    Spark the interest in what python brings to the test automation table and maybe join the community. That’s it, really.
    You don’t need to be a programming expert to start writing automated software. Thou as every professional you need
    to have the basic understanding of the syntax, class structure, mutability and variable scope, object instantiation. 

1. What you need to know in order to navigate and understand the code:
    
    **PYTHON** (latest stable version will do the job or at least 3.6+)
    You don’t need to know a lot of Python. The examples don’t do anything super weird or fancy. If you know at least
    functional programming in python you should have no problems in navigating and understanding the code. Or in case 
    come from a Java / C# community you should be able to navigate easily through the code logic. Python can be used both 
    in a traditional OOP manner and functional. For the sake of simplicity I have broken down the logic blocs mainly 
    into functions.
    
    **PIP** (comes out of the box together with your python installation)
    You should use pip to install pytest and pytest plugins as this is the official packet manager for python. 
    If you want a refresher on pip check out https://pip.pypa.io/en/stable. 
    
    **A COMMAND LINE**
    I wrote this demo using bash on a Linux distribution OS. However, the only commands I use in bash are cd to go to a
    specific directory, and pytest, of course. Since cd exists in Windows cmd.exe and all unix shells that I know of,
    all examples should be runnable on whatever terminal-like application you choose to use.
    
    **An IDE you feel comfortable with**
    You can either use VS code, or a dedicated platform like Pycharm, Anaconda. Even Sublimetext will do as it can be
    tweaked with python specific plugins and turned into a full featured python IDE. The code and followup project presentation
    have been made in Pycharm. But again this is more a matter of personal preference and habit. The choice is entirely yours.
   
    **ACCESS**
    to the repo where the project is stored and available for public download / fork.

    **OFFICIAL DOCS** 
    - pytest docs with examples: https://docs.pytest.org/en/6.2.x/
    - pytest-bdd docs with examples: https://pypi.org/project/pytest-bdd/
    - quick start guide: https://www.amazon.com/pytest-Quick-Start-Guide-maintainable-ebook/dp/B07GZJD473
    - start-to-end guide: https://www.amazon.com/Python-Testing-pytest-Effective-Scalable-ebook/dp/B0773VRHWT
    - summary on pytest cli params and usage explanation: https://cheatography.com/nanditha/cheat-sheets/pytest/
    - podcasts and conference materials: https://docs.pytest.org/en/6.2.x/talks.html
    - pytest related libraries (plugins): https://docs.pytest.org/en/latest/reference/plugin_list.html


2. How to set up your environment and get the resource code
    Install python from the official site (https://www.python.org/downloads/). There you will find details instruction 
    with respect to the OS you choose to work on. When completed, you should perform in console `"python --version"`, then
    you should get the version of your installation
    Git clone the project form the provided repo link.
    A good practice is to have for your project dependencies stored in a virtual environment, therefore 
    bounded only to your project and without an impact on your entire OS. For more detailed info you can consult the official 
    documentation at https://docs.python.org/3/library/venv.html and the user guide at https://docs.python-guide.org/dev/virtualenvs/.
    Generate your own virtual environment for the project with the following commands:
    ``` 
    > pip3 install -U virtualenv (will install the virtualenv packadge)
    > python3 -m virtualenv venv (will generate the folder with the fiels for your virtual environment)
    > source venv/bin/activate (will activate the virtual ennvironment). In this mode python interpereter and pip 
    installed in the system will handle all project dependecies locally in the "./venv/" folder.
    > pip install ... (isntall the needed dependecies) Being in the virtual env, install pytest, pytest-bdd libraries 
    and the rest of dependencies we need. The needed dependencies are listed in file "requirements.txt". 
    You can install each dependency manually (ex. pip install pytest) or you can use command `"pip install -r requirements.txt"` 
    so that pip reads the respective file and install every library with the respective needed version listed there automatically.
   ```

3. Intro into the demo app
    In order to materialize the theory into practice I have crafted a very simple api app written with flask library. 
    You can find it in the root directory of the cloned project at app/serve.py. It exposed one endpoint only "companies" 
    that responds to 2 http method calls `"GET" and "POST"`.
    All this endpoint does is reads from a json file (in real life app this would be a 
    database, but for the sake of simplicity a file will do just fine) when called through the GET method, and writes 
    to it new records when called through the POSTS method. Also, we have defined some handlers for the 404 and 400 situations.
    The json file "db.json" is in the same location folder as the app, there you can see the pre-defined records and also
    'db_bkp.son' that is just a backup of the db that we will use further in our tests

4. Present the test cases list:
    1. Get all the records
    2. Get a specific record id
    3. Get a record with invalid id (that does not exist )
    4. Get a record with invalid id (that is not in the correct format)
    5. Post a new item with sufficient fields
    6. Post a new item with id pre-defined in the request payload
    7. Post a new item with insufficient fields 
    8. Post a new item with more fields than defined by the requirements
    

6. A bit of theory on fixtures, test parametrisation and more


7. What is pytest
    - short history at https://docs.pytest.org/en/latest/history.html and link to the founder of moder day pytest: https://twitter.com/hpk42 
    - Architecture and abstraction API: https://docs.pytest.org/en/6.2.x/reference.html. Pytest initiates special stages and scopes when run:
        - Initial config Load
        - Collect test run options 
        - Test Collection / Fixture objects loading and scope definition 
        - Test Running (single thread, multi thread distributed)
        - Test Status Reporting and report aggregation
        - Debug Reporting
    
    The key takeaway from this should be  that you can basically customise each step of test execution.
    Starting form test collection/ filtering and naming and ending the test reporting phase.
      
    Some basic commands and explanations to them :
    ```
    > pytest --help -> get the help documentation on pytest usage options
    > pytest {path} -> call pytest with the absolute/relative path to the test location (either file of folder, subfolders).
    The naming convention for the test entities to be collected is:
        Test files should be named test_<something>.py or <something>_test.py.
        Test methods and functions should be named test_<something>.
        Test classes should be named Test<Something>.
    After the tests have been collected > they are run > the test output is being generated
    Here are the possible outcomes of a test function:
        PASSED (.): The test ran successfully.
        FAILED (F): The test did not run successfully (or XPASS + strict).
        SKIPPED (s): The test was skipped. You can tell pytest to skip a test by using either the
        @pytest.mark.skip() or pytest.mark.skipif() decorators, discussed in Skipping Tests .
        xfail (x): The test was not supposed to pass, ran, and failed. You can tell pytest that a test
        is expected to fail by using the @pytest.mark.xfail() decorator, discussed in Marking Tests
        as Expecting to Fail .
        XPASS (X): The test was not supposed to pass, ran, and passed.
        ERROR (E): An exception happened outside of the test function (preparation/teardown steps)
    > You can run a bunch of tests or a single test
    > pytest -v {path}/ --verbose {path} -> call pytest with verbose mode on
    > pytest -vv test_one.py call pytest with "very verbose" mode on
    > pytest --collect-only -> option shows you which tests will be run with the given options and configuration.
    Does not actually run the tests, only collects it
    >  pytest -k "<bool expression>" --collect-only -> -k option lets you use an expression to find what test functions to run.
    > pytest -m <MARKEXPR> -> Markers (or tags) are one of the best ways to mark a subset of your test functions so that they can be run
    together. As an example, one way to run certain tests, even though they are in separate files, is to mark them. You
    can use any marker name. Let’s say you want to use run_these_please. You’d mark a test using the decorator
    @pytest.mark.run_these_please, So when collecting the functions to execute, pytest will select only the test
    functions / classes that mathc the respective expression
    > pytest -x / --exitfirst -> stopping the entire test session immediately when a test fails.
    Useful for test debugging purposes
    > pytest --maxfail={num} -> as previously stated -x option stops after one test failure. If you want to let some
    failures happen, but not every single one of them, use the --maxfail option to specify how many failures are okay with you.
    ```

8. Present standard implementation of the pytest suite of tests, with everything that 
comes from it, pytest.ini, conftest.py, helper modules, hooks overriding

10. Present custom implementation of the pytest suite of test, that would show 
how to separate test data form actual implementation of your tests and create your own custom data format

11. Q&A session (15-20 minutes max should be allocated)
