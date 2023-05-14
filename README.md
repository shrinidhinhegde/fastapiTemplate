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

<p>The Project working directory is the <code>src</code> directory. The root folder only contains <code>poetry</code> and <code>docker</code> config files. Hence, all the <code>alembic</code> and <code>FastAPI</code> commands can be run only from the working directory</p>

<h4>Add a <code>.env</code> file inside the working directory (you can find an example at <code>
.env.example</code>)</h4>

<p>Install the project dependencies using the following command:</p>
<pre>
poetry install
</pre>
<p>this command automatically creates a virtual environment and then installs the dependencies</p>
<p>Poetry virtual environment can be activated using</p>
<pre>
source $(poetry env info --path)/bin/activate
</pre>
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
docker-compose up
</pre>

<p>The database migrations has to be applied by running <code>alembic upgrade head</code>. If you are using docker, run this command in <code>app-web-server</code> container</p>

<p>The API documentation can be accessed <a href="https://localhost:8000/docs">here</a></p>

<h2>Database migrations using alembic</h3>

<p>To generate migration files run the following command</p>
<pre>
alembic revision --autogenerate -m "migration message"
</pre>

<p>After generating the migration files, run the following command to migrate models</p>
<pre>
alembic upgrade head
</pre>

<p>Note - Alembic is not 100% accurate always so check migration file manually and make corrections if needed</p>
<p>Refer alembic documentation <a href="https://alembic.sqlalchemy.org/en/latest/">here</a></p>