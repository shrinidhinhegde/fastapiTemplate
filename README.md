<h1>App Backend</h1>

<p>Template for fastapi backend. This project has been configured using <a href="https://python-poetry.org">poetry</a>.</p>

<h2>Poetry Installation</h2>

<p>Install poetry using the following command:</p>

<pre>
pip install poetry
</pre>

<p>Verify installation using the following command:</p>

<pre>
poetry --version
</pre>

<h2>Project Installation</h2>

<p>The Project working directory is the <code>src</code> directory. The root folder only contains <code>poetry</code> 
and <code>docker</code> config files. Hence, all the <code>alembic</code> and <code>FastAPI</code> commands can 
be run only from the working directory</p>

<h4>Add a <code>.env</code> file inside <code>env_config</code> the working directory (you can find an example at <code>
.env.example</code>)</h4>

<p>Install the project dependencies using the following command:</p>
<pre>
poetry install
</pre>
<p>this command automatically creates a virtual environment and then installs the dependencies</p>
<p>Poetry virtual environment can be activated using</p>
<pre>
poetry run activate
</pre>
<p>or alternatively use <code>source $(poetry env info --path)/bin/activate</code></p>
<p>and run:</p>
<pre>
python main.py
</pre>

<p>A local postgres database has to be set up.</p>
<p>
If your IDE wants a virtual environment configured, run <code>poetry env info</code>
and copy the path of the virtual environment and paste it into your IDE's configuration.
</p>
<p>NOTE: If you are facing <code>ModuleNotFoundError: No module named 'src'</code> set the env variable <code>PYTHONPATH</code> using <code>export PYTHONPATH="${PYTHONPATH}:/path/to/approot"</code> and you can use <code>set PYTHONPATH="${PYTHONPATH}:/path/to/approot"</code> on a windows machine</p>

<h3>Alternatively</h3>

<p><code>docker-compose.yaml</code> is configured with a persistent database volume which is retained in your system unless cleared explicitly and the server and local database can be started using the following command:</p>
<pre>
poetry run local
</pre>
<p>or alternatively <code>docker-compose up -d</code></p>

<p>The database migrations has to be applied by running <code>poetry run migrate</code>. If you are using docker, run this command in <code>app-web-server</code> container</p>

<p>The API documentation can be accessed <a href="https://localhost:8000/docs">here</a></p>

<h2>Packages</h2>

<p>Few packages have already been added to the project.</p>

<p>You can add new packages using the following command</p>

<pre>
poetry add {package-name}
</pre>

<p>If you wish to add a package as a dev dependency. Use the following command</p>

<pre>
poetry add --group dev {package-name}
</pre>

<h2>Database migrations using alembic</h3>

<p>To generate migration files run the following command</p>
<pre>
poetry run make_migrations
</pre>
<p>alternatively, you can use <code>alembic revision --autogenerate -m "migration message"</code></p>

<p>After generating the migration files, run the following command to migrate models</p>
<pre>
poetry run migrate
</pre>
<p>or alternatively <code>alembic upgrade head</code></p>

<p>Note - Alembic is not 100% accurate always so check migration file manually and make corrections if needed</p>
<p>Refer alembic documentation <a href="https://alembic.sqlalchemy.org/en/latest/">here</a></p>

<h2>Versioning</h2>

<p>You can use the <code>poetry version</code> command to automatically bump the version of your project. Here's an example of how to
use it to bump the patch version: </p>

<pre>
poetry version patch
</pre>

<p>This will update the version number in your <code>pyproject.toml</code> file and create a new commit with the updated
version
number.</p>

<p>You can also use <code>minor</code> or <code>major</code> instead of <code>patch</code> to bump the minor or major version, respectively.</p>

<pre>
poetry version patch
git add [files]
git commit -m "commit message"
git tag $(poetry version --short)
</pre>

<p>This will create a new commit with the updated version number and a new git tag with the same version number.</p>

<h2>Testing</h2>

<p>Testing has been set up using <code>httpx</code> and <code>pytest-asyncio</code>. Test can be found under <code>tests</code> package</p>

<p>Testing will be done on a test database which needs to be configured on the same host. The name of the database has to be added to .env as <code>POSTGRES_TEST_DB</code></p>

<p>Run the following command to run all the tests</p>
<pre>
poetry run tests
</pre>
<p>or alternatively run <code>pytest {file_name}</code> to run particular test module</p>

<p>Test fixtures can be configured in <code>tests/conftest.py</code></p>
<p>NOTE: All the test files must be of the format <code>test_*.py</code> and can use the <code>test_client</code> found in <code>test_main.py</code></p>

<h2>Celery - Redis</h2>

<p>Celery worker and a redis server has been set up in <code>docker-compose.yaml</code></p>

<p>Follow <a href="https://www.jetbrains.com/pycharm/guide/tutorials/fastapi-aws-kubernetes/redis_celery/">this blog</a> to setup a redis server locally</p>
<p>Celery worker can be created using the following command:</p>
<pre>
celery -A main.celery worker -B -l info
</pre>

<p>Celery tasks can be configured but the path to these tasks have to be added in <code>celery.conf.imports</code> in <code>src/main.py</code>. And once new tasks are added. The celery workers have to be restarted.</p>

<p>The tasks can be started by using <code>.delay()</code> method.</p>

<h2>Code Formatting</h2>

<p><code>black</code> python formatter added and project is using default configurations.</p>
<p>To format all the files in the project, you can run:</p>
<pre>
poetry run lint
</pre>


<p>or alternatively, <code>black {source_file_or_directory}</code></p>
<p>Make sure to run the formatter before committing the files. You can configure your IDE to auto format everytime you save your file.</p>


<h2>Debugging</h2>

<p>Python - Ice Cream has been installed in this project as a dev dependency. You can use the <code>ic()</code> to debug you code.</p>
<p>For more info <a href="https://github.com/gruns/icecream">visit</a></p>