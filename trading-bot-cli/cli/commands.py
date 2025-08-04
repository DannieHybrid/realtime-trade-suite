import click
import requests

JUPITER_QUOTE_API = "https://quote-api.jup.ag/v6/quote"

@click.group()
def cli():
    pass

@cli.command()
@click.option('--input-token', required=True, help='Input token mint')
@click.option('--output-token', required=True, help='Output token mint')
@click.option('--amount', required=True, type=int, help='Amount (in smallest unit)')
def quote(input_token, output_token, amount):
    """Get quote for token swap"""
    params = {
        "inputMint": input_token,
        "outputMint": output_token,
        "amount": amount,
    }

    try:
        res = requests.get(JUPITER_QUOTE_API, params=params)
        click.echo(f"\n🔍 Request URL: {res.url}")
        click.echo(f"📡 Status Code: {res.status_code}")

        if res.status_code == 200:
            data = res.json()
            click.echo("✅ Quote response:")
            click.echo(data)
        else:
            click.echo("❌ Failed to fetch quote:")
            click.echo(res.text)

    except Exception as e:
        click.echo(f"🚨 Exception occurred: {e}")
