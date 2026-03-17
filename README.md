# ZenithAI
An experimental AI helper for visibility and targeting inquiries.

## Install

Create the virtual environment and install dependencies:

```powershell
uv sync
```

The project uses `langchain-openai` to connect to OpenAI models.

Set your OpenAI API key before starting the app:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

## Run

Start the chat interface:

```powershell
uv run zenithai
```

You can also run the package module directly:

```powershell
uv run python -m zenithai
```

After startup, type your message at the `You>` prompt.
Type `exit` or `quit` to end the session.

## Configuration

ZenithAI reads runtime configuration from environment variables.

- `ZENITHAI_STELLARIUM_BASE_URL`
- `ZENITHAI_TIMEOUT`
- `ZENITHAI_MODEL`

Example:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
$env:ZENITHAI_STELLARIUM_BASE_URL="http://localhost:8090/api"
$env:ZENITHAI_TIMEOUT="10"
$env:ZENITHAI_MODEL="openai:gpt-5.2"
uv run zenithai
```

## Test

Run the test suite with:

```powershell
python -m unittest discover -s tests -v
```
