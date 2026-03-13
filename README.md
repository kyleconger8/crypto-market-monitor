# Cryptocurrency Market Monitor (Athena AI Challenge)

This project implements an Athena AI Agent that monitors cryptocurrency prices using a public data source.

## Architecture

Athena Agent  
↓  
MCP Server (Flask)  
↓  
CoinGecko Public API  
↓  
Interactive Widget  

## Features

• Real-time cryptocurrency price retrieval  
• MCP server exposing crypto data endpoint  
• Interactive widget inside Athena  
• Dropdown selection of cryptocurrencies  
• Refresh button to update prices  

## Endpoint

GET /crypto?coins=bitcoin,ethereum

Example response:

{
 "bitcoin": {
  "usd": 68000,
  "usd_24h_change": 1.2
 }
}

## Technologies

Python  
Flask  
CoinGecko API  
Athena MCP  
HTML / JavaScript widget

## Deployment

Deploy the MCP server using Render or another cloud service.

Start command:

gunicorn server:app

Example MCP URL:

https://your-service.onrender.com/crypto
