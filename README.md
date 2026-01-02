# StockBro - Real-time Financial Dashboard

A powerful **web-based** financial dashboard for real-time stock and cryptocurrency monitoring, powered by **Polygon.io API** (rebranded to Massive), **Alpha Vantage API**, and **xAI Grok 4.1 Fast** reasoning. Built with **Dash (Plotly)** for interactive web visualization. Optimized for reliability and performance as of December 2025.

---

## What is StockBro?

**StockBro** is a comprehensive, real-time financial data visualization platform that combines traditional market data with cutting-edge AI-powered sentiment analysis. It's a fully-featured web application that transforms raw financial data into actionable insights through interactive charts, technical indicators, news analysis, and AI-driven market sentiment evaluation.

Unlike command-line tools or static reports, StockBro provides an intuitive, browser-based interface that makes financial analysis accessible to both technical and non-technical users. Whether you're monitoring a single stock, tracking cryptocurrency movements, or analyzing market sentiment, StockBro delivers professional-grade financial analysis tools in an easy-to-use package.

---

## What Does It Do?

StockBro aggregates and visualizes financial data from multiple sources, providing:

### Core Functionality

- **📊 Real-Time Market Monitoring**: Track live prices for stocks and cryptocurrencies with WebSocket streaming (Polygon) or polling (Alpha Vantage)
- **📈 Historical Data Analysis**: Visualize 30 days of OHLCV (Open, High, Low, Close, Volume) data with interactive charts
- **🕯️ Advanced Charting**: Multiple chart types including line charts, candlestick charts, and volume analysis
- **📰 News Integration**: Fetch and display recent news articles related to your selected asset with clickable links
- **💭 Sentiment Analysis**: Three-tier sentiment analysis system:
  - **xAI Grok 4.1 Fast**: AI-powered reasoning with step-by-step analysis traces
  - **Alpha Vantage**: Built-in AI sentiment scores
  - **Keyword-Based**: Fast sentiment analysis using positive/negative word detection
- **📉 Technical Indicators**: Professional technical analysis tools:
  - RSI (Relative Strength Index) with overbought/oversold markers
  - MACD (Moving Average Convergence Divergence)
  - Bollinger Bands for volatility analysis
  - Moving averages (7-day and 30-day)
- **📋 Interactive Data Tables**: Sortable, scrollable tables with complete historical data
- **🌙 Dark Mode**: Comfortable viewing in any lighting condition
- **🔄 Auto-Refresh**: Optional automatic updates every 60 seconds for real-time monitoring

### Key Features

- **Dual Data Source Support**: Choose between Polygon.io (premium features, WebSocket streaming) or Alpha Vantage (free tier, built-in sentiment)
- **Multi-Asset Support**: Monitor both traditional stocks (NYSE, NASDAQ) and cryptocurrencies (Bitcoin, Ethereum, etc.)
- **Thread-Safe Architecture**: Secure concurrent updates for real-time data streaming
- **Robust Error Handling**: Graceful degradation and clear error messages
- **Rate Limit Management**: Automatic rate limiting to respect API constraints
- **Zero Configuration Required**: Works out of the box with API keys

---

## Who Is This For?

StockBro is designed for a diverse range of users:

### 🎯 Primary Users

1. **Individual Investors & Traders**
   - Day traders monitoring real-time price movements
   - Swing traders analyzing technical indicators and sentiment
   - Long-term investors tracking portfolio positions
   - Crypto enthusiasts following digital asset markets

2. **Financial Analysts & Researchers**
   - Market researchers needing quick data visualization
   - Analysts comparing sentiment across different sources
   - Students learning financial analysis techniques
   - Journalists writing market analysis pieces

3. **Developers & Data Scientists**
   - Developers building financial applications
   - Data scientists prototyping trading strategies
   - FinTech startups needing a dashboard solution
   - Hobbyists exploring financial APIs

4. **Educators & Students**
   - Finance professors teaching market analysis
   - Students learning about technical analysis
   - Coding bootcamp participants building portfolio projects
   - Self-learners exploring financial technology

### 👥 User Profiles

- **The Casual Investor**: Wants to quickly check stock prices and recent news without complexity
- **The Active Trader**: Needs real-time data, technical indicators, and sentiment analysis for trading decisions
- **The Researcher**: Requires comprehensive data visualization and analysis tools
- **The Developer**: Wants a clean, well-documented codebase to build upon or integrate
- **The Learner**: Seeking to understand financial markets through hands-on visualization

---

## Why Use StockBro?

### 🎯 Problem It Solves

The financial data landscape is fragmented and complex. Getting comprehensive market information typically requires:
- Multiple subscriptions to expensive services
- Complex API integrations
- Technical expertise to build custom tools
- Time-consuming data aggregation from various sources

**StockBro solves this by providing a single, unified platform that combines:**
- Real-time price data
- Historical analysis
- News aggregation
- AI-powered sentiment analysis
- Technical indicators
- Professional visualizations

### ✨ Key Benefits

1. **🚀 Quick Setup, Zero Complexity**
   - Install dependencies, add API keys, and you're running in minutes
   - No complex configuration or infrastructure required
   - Web-based interface means no app installations needed

2. **💰 Cost-Effective**
   - Works with free-tier API keys (Alpha Vantage offers free access)
   - No subscription fees or hidden costs
   - Self-hosted means you control your data and costs

3. **🔒 Privacy & Security**
   - Runs locally on your machine
   - API keys stored securely (environment variables)
   - No data sent to third-party servers (except API providers)
   - Open-source code you can audit

4. **🎨 Professional Visualizations**
   - Interactive Plotly charts with zoom, pan, and hover details
   - Publication-ready visualizations
   - Export capabilities for reports and presentations

5. **🤖 AI-Powered Insights**
   - Optional xAI Grok integration for advanced sentiment analysis
   - Step-by-step reasoning traces for transparency
   - Multiple sentiment analysis methods for comparison

6. **🔄 Flexible & Extensible**
   - Support for multiple data sources (switch between Polygon and Alpha Vantage)
   - Modular architecture makes customization easy
   - Well-documented codebase for developers

7. **📱 Accessible Anywhere**
   - Web-based interface works on any device with a browser
   - Run locally or deploy to a server for remote access
   - Responsive design adapts to different screen sizes

### 🎓 Use Cases

- **Portfolio Monitoring**: Track your holdings in real-time with automatic refresh
- **Market Research**: Analyze historical trends and sentiment for investment decisions
- **Trading Strategy Development**: Test technical indicators and sentiment analysis
- **News-Driven Trading**: Monitor news and sentiment before making trades
- **Educational Projects**: Learn about financial markets through interactive visualization
- **Due Diligence**: Quick analysis of assets before investment
- **Market Timing**: Identify entry and exit points using technical indicators
- **Crypto Trading**: Monitor cryptocurrency markets with the same tools as stocks

---

## Features

- **🌐 Web-Based Interface**: Interactive Dash (Plotly) web dashboard - no command line needed!
- **Dual Data Source Support**: Choose between Polygon.io or Alpha Vantage APIs
- **Real-time Price Updates**: WebSocket streaming for live price updates (Polygon only; Alpha Vantage uses polling)
- **Historical Data Analysis**: Fetch and visualize OHLCV data with interactive tables
- **Interactive Charts**: Plotly-powered charts with zoom, pan, and hover details
- **News Integration**: Fetch recent news articles with clickable links
- **Advanced Sentiment Analysis**: 
  - **xAI Grok 4.1 Fast reasoning** for AI-powered sentiment with step-by-step traces
  - Built-in AI sentiment scores with Alpha Vantage NEWS_SENTIMENT
  - Keyword-based sentiment analysis for Polygon
- **AI-Powered Market Analysis**: Grok 4.1 Fast provides reasoned insights, trends, and forecasts
- **Multi-Asset Support**: Works with both stocks (e.g., AAPL) and cryptocurrencies (e.g., BTC-USD)
- **Technical Indicators**: RSI, MACD, Bollinger Bands, and moving averages
- **Thread-Safe**: Secure concurrent updates for real-time data
- **Error Handling**: Robust error handling and reconnection logic
- **Rate Limit Management**: Automatic rate limiting for Alpha Vantage (5 calls/minute free tier)
- **Auto-Refresh**: Optional automatic updates every 60 seconds
- **Dark Mode**: Comfortable viewing in any lighting condition

---

## System Requirements

### Minimum Requirements

- **Operating System**: 
  - macOS 10.14+ (Mojave or later)
  - Windows 10/11
  - Linux (Ubuntu 18.04+, Debian 10+, Fedora 30+, or similar)
- **Python**: 3.8 or higher (3.10+ recommended)
- **RAM**: 512 MB minimum (1 GB recommended)
- **Disk Space**: 200 MB for installation
- **Internet Connection**: Required for API calls and Plotly CDN

### Recommended Requirements

- **Python**: 3.10 or higher
- **RAM**: 2 GB or more
- **Disk Space**: 500 MB
- **Processor**: Modern multi-core processor
- **Browser**: Latest version of Chrome, Firefox, Safari, or Edge

### API Keys Required

- **Polygon.io API key** (get one at [massive.com](https://massive.com) - formerly polygon.io) **OR**
- **Alpha Vantage API key** (get one at [alphavantage.co](https://www.alphavantage.co/support/#api-key) - free tier: 25 calls/day, 5 calls/minute)
- **xAI API key** (optional, get one at [x.ai/api](https://x.ai/api) - for Grok 4.1 Fast reasoning)

**Note**: You only need ONE data source API key (either Polygon OR Alpha Vantage). xAI Grok is completely optional.

---

## Complete Installation Guide

### Step 1: Verify Python Installation

First, check if Python is installed and which version:

```bash
python3 --version
# or
python --version
```

**Expected output**: Python 3.8.0 or higher

**If Python is not installed**:

- **macOS**: Install via Homebrew: `brew install python3` or download from [python.org](https://www.python.org/downloads/)
- **Windows**: Download installer from [python.org](https://www.python.org/downloads/) - check "Add Python to PATH" during installation
- **Linux (Ubuntu/Debian)**: `sudo apt-get update && sudo apt-get install python3 python3-pip python3-venv`
- **Linux (Fedora)**: `sudo dnf install python3 python3-pip`

### Step 2: Clone the Repository

#### Option A: Clone via Git (Recommended)

```bash
git clone https://github.com/seanebones-lang/stockbro.git
cd stockbro
```

#### Option B: Download ZIP

1. Visit [GitHub repository](https://github.com/seanebones-lang/stockbro)
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal/command prompt in the extracted folder

### Step 3: Create Virtual Environment

**Why use a virtual environment?** It isolates dependencies and prevents conflicts with other Python projects.

#### macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

#### Windows:

```cmd
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your command prompt.

#### Verify Virtual Environment is Active

```bash
which python  # macOS/Linux
where python  # Windows
```

The output should point to the `venv` directory.

### Step 4: Upgrade pip (Recommended)

```bash
python -m pip install --upgrade pip
```

This ensures you have the latest pip version for smooth installation.

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

**What this installs**:
- `polygon-api-client` (v1.14+) - For Polygon REST API and WebSocket connections
- `pandas` (v2.0+) - For data processing and analysis
- `matplotlib` (v3.7+) - For charting and visualization
- `numpy` (v1.24+) - For numerical operations
- `requests` (v2.31+) - For Alpha Vantage API calls
- `xai-sdk` (v1.0+) - For xAI Grok 4.1 Fast reasoning (optional)
- `dash` (v2.14+) - For web interface (Plotly Dash framework)
- `plotly` (v5.17+) - For interactive charts

**Expected installation time**: 1-3 minutes depending on internet speed

**Troubleshooting installation issues**: See [Troubleshooting](#troubleshooting) section below.

### Step 6: Verify Installation

Test that all packages are installed correctly:

```bash
python -c "import dash, plotly, pandas, numpy, requests; print('All core packages installed successfully!')"
```

**Expected output**: `All core packages installed successfully!`

Optional test for Polygon and xAI:

```bash
python -c "from polygon import RESTClient; print('Polygon package OK')"
python -c "import xai_sdk; print('xAI package OK')"  # Optional
```

### Step 7: Set Up API Keys

You need at least one API key to use StockBro. Choose based on your needs:

- **Alpha Vantage**: Free tier available, good for beginners
- **Polygon**: Better for real-time features, paid plans available
- **xAI Grok**: Optional, enhances sentiment analysis

#### Option A: Environment Variables (Recommended for Persistent Use)

This method stores API keys securely and avoids entering them each time.

**macOS/Linux**:

Add to `~/.bashrc`, `~/.zshrc`, or `~/.profile`:

```bash
# Add these lines to your shell configuration file
export POLYGON_API_KEY="your_polygon_api_key_here"
export ALPHAVANTAGE_API_KEY="your_alphavantage_api_key_here"
export XAI_API_KEY="your_xai_api_key_here"  # Optional
```

Then reload your shell:

```bash
source ~/.bashrc  # or source ~/.zshrc
```

**Windows (PowerShell)**:

```powershell
[System.Environment]::SetEnvironmentVariable('POLYGON_API_KEY', 'your_key_here', 'User')
[System.Environment]::SetEnvironmentVariable('ALPHAVANTAGE_API_KEY', 'your_key_here', 'User')
[System.Environment]::SetEnvironmentVariable('XAI_API_KEY', 'your_key_here', 'User')  # Optional
```

Restart PowerShell for changes to take effect.

**Windows (Command Prompt)**:

```cmd
setx POLYGON_API_KEY "your_key_here"
setx ALPHAVANTAGE_API_KEY "your_key_here"
setx XAI_API_KEY "your_key_here"  # Optional
```

**Verify environment variables are set**:

```bash
echo $POLYGON_API_KEY  # macOS/Linux
echo %POLYGON_API_KEY%  # Windows CMD
$env:POLYGON_API_KEY  # Windows PowerShell
```

#### Option B: Enter in Web Interface

If you don't set environment variables, you can enter API keys directly in the web interface when prompted. Note: You'll need to re-enter them each session.

### Step 8: Test the Installation

Run a quick test to ensure everything works:

```bash
python financial_dashboard.py
```

**Expected output**:
```
============================================================
Financial Dashboard - Web Interface
Powered by Dash (Plotly)
============================================================

Starting web server...
Open your browser and navigate to: http://127.0.0.1:8050
Press Ctrl+C to stop the server
============================================================
Dash is running on http://127.0.0.1:8050/
```

If you see this, installation is successful! Press `Ctrl+C` to stop the server.

---

## Running the Application

### Method 1: Direct Python Execution

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

python financial_dashboard.py
```

### Method 2: Using the Convenience Script (macOS/Linux)

```bash
chmod +x run_dashboard.sh
./run_dashboard.sh
```

This script automatically activates the virtual environment and starts the server.

### Method 3: Run in Background (Advanced)

**macOS/Linux**:

```bash
nohup python financial_dashboard.py > dashboard.log 2>&1 &
```

**Windows**:

Use PowerShell:

```powershell
Start-Process python -ArgumentList "financial_dashboard.py" -WindowStyle Hidden
```

### Accessing the Dashboard

1. Open your web browser
2. Navigate to: `http://127.0.0.1:8050`
3. The dashboard interface should load

**Note**: The dashboard runs on your local machine. To access from other devices on your network, you'll need to modify the host in `financial_dashboard.py` (change `host='127.0.0.1'` to `host='0.0.0.0'`).

---

## Configuration

### Changing the Port

If port 8050 is in use, you can change it by editing `financial_dashboard.py`:

```python
# Find this line near the end of the file:
app.run(debug=True, host='127.0.0.1', port=8050)

# Change to your desired port (e.g., 8080):
app.run(debug=True, host='127.0.0.1', port=8080)
```

### Changing the Host (Network Access)

To allow access from other devices on your network:

```python
# Change from:
app.run(debug=True, host='127.0.0.1', port=8050)

# To:
app.run(debug=True, host='0.0.0.0', port=8050)
```

**Security Note**: Only use `0.0.0.0` on trusted networks. For production, use proper authentication and HTTPS.

### Disabling Debug Mode

For production use, disable debug mode:

```python
app.run(debug=False, host='127.0.0.1', port=8050)
```

---

## Troubleshooting

### Installation Issues

#### Problem: "command not found: python3" or "python is not recognized"

**Solution**: 
- Verify Python is installed: `python --version` or `python3 --version`
- On Windows, ensure Python is added to PATH during installation
- On macOS, install via Homebrew: `brew install python3`
- On Linux, install: `sudo apt-get install python3` (Ubuntu/Debian) or `sudo dnf install python3` (Fedora)

#### Problem: "pip: command not found"

**Solution**:
- Install pip: `python -m ensurepip --upgrade`
- On Linux: `sudo apt-get install python3-pip` (Ubuntu/Debian) or `sudo dnf install python3-pip` (Fedora)
- On macOS: `python3 -m ensurepip --upgrade`

#### Problem: "Permission denied" when installing packages

**Solution**:
- Use virtual environment (recommended): `python -m venv venv && source venv/bin/activate`
- Don't use `sudo` with pip when using a virtual environment
- If you must use system Python, you might need `sudo` but this is not recommended

#### Problem: "ERROR: Could not find a version that satisfies the requirement"

**Solution**:
- Upgrade pip: `python -m pip install --upgrade pip`
- Check Python version: `python --version` (must be 3.8+)
- Try installing packages individually to identify the problematic package
- Check internet connection

#### Problem: Installation takes too long or hangs

**Solution**:
- Check internet connection
- Use a different pip index: `pip install -r requirements.txt -i https://pypi.org/simple`
- Install packages one at a time to identify the problematic package
- On Windows, try running as administrator
- On Linux, ensure you have build tools: `sudo apt-get install build-essential python3-dev`

### Runtime Issues

#### Problem: "Address already in use" or "Port 8050 is in use"

**Solution**:
```bash
# Find process using port 8050
# macOS/Linux:
lsof -ti:8050 | xargs kill -9

# Windows (PowerShell):
Get-NetTCPConnection -LocalPort 8050 | Select-Object -ExpandProperty OwningProcess | ForEach-Object { Stop-Process -Id $_ -Force }

# Or change the port in financial_dashboard.py (see Configuration section)
```

#### Problem: "ModuleNotFoundError: No module named 'X'"

**Solution**:
- Ensure virtual environment is activated (you should see `(venv)` in prompt)
- Reinstall dependencies: `pip install -r requirements.txt`
- Verify installation: `pip list | grep X` (replace X with module name)

#### Problem: Dashboard loads but shows "No data available"

**Solution**:
- Verify API key is set: `echo $POLYGON_API_KEY` (or `$ALPHAVANTAGE_API_KEY`)
- Check API key is valid by testing it manually
- Ensure you've entered a valid ticker symbol (e.g., `AAPL` for stocks, `BTC-USD` for crypto)
- Check internet connection
- Verify you haven't exceeded API rate limits
- Check browser console (F12) for JavaScript errors

#### Problem: "Error fetching historical data"

**Solution**:
- Verify API key is correct and valid
- Check ticker symbol is valid (e.g., `AAPL` not `apple`)
- Ensure API key has sufficient credits/quota
- Check API service status (Polygon.io or Alpha Vantage status page)
- Verify internet connection
- Try a different ticker symbol to rule out ticker-specific issues

#### Problem: "No real-time updates" (WebSocket not working)

**Solution**:
- Verify you're using Polygon.io (Alpha Vantage doesn't support WebSocket)
- Check your Polygon API plan includes WebSocket access
- Ensure "Real-Time Updates" toggle is enabled in the dashboard
- Check network connectivity (WebSocket requires stable connection)
- Verify ticker is actively traded (some symbols may have limited data)

#### Problem: Charts not displaying

**Solution**:
- Check internet connection (Plotly uses CDN for JavaScript)
- Clear browser cache and reload page
- Check browser console (F12) for JavaScript errors
- Try a different browser (Chrome, Firefox, Safari, Edge)
- Disable browser extensions that might interfere
- Verify Plotly is installed: `pip list | grep plotly`

#### Problem: "Alpha Vantage rate limit" error

**Solution**:
- Wait 12 seconds between API calls (script should do this automatically)
- You've exceeded 5 calls/minute limit - wait 1 minute
- You've exceeded 25 calls/day limit - wait until tomorrow or upgrade plan
- Consider switching to Polygon.io for higher rate limits
- Use the manual refresh button instead of auto-refresh to control call frequency

#### Problem: "xAI Grok error" or Grok not working

**Solution**:
- Verify xAI API key is correct: `echo $XAI_API_KEY`
- Check xAI account has available credits
- Ensure xai-sdk is installed: `pip install xai-sdk`
- Check xAI service status
- Grok is optional - the dashboard will fall back to basic sentiment analysis
- Check xAI API rate limits haven't been exceeded

#### Problem: Virtual environment not activating

**Solution**:

**macOS/Linux**:
```bash
# If you get "command not found: source"
bash venv/bin/activate  # Try with bash explicitly

# Or recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
```

**Windows**:
```cmd
# If activation script doesn't run
venv\Scripts\activate.bat  # Try .bat explicitly

# Or in PowerShell, you may need to allow scripts:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Problem: "SSL certificate verification failed"

**Solution**:
```bash
# Update certificates (macOS)
/Applications/Python\ 3.*/Install\ Certificates.command

# Or install certifi package
pip install --upgrade certifi

# Linux - update CA certificates
sudo apt-get update && sudo apt-get install ca-certificates
```

#### Problem: Dashboard is slow or unresponsive

**Solution**:
- Check internet connection speed
- Disable xAI Grok if enabled (adds latency)
- Reduce auto-refresh frequency
- Close other applications using network/CPU
- Check system resources (CPU, RAM usage)
- Try a different data source (Polygon vs Alpha Vantage)

### API Key Issues

#### Problem: API key not recognized

**Solution**:
- Verify environment variable is set: `echo $POLYGON_API_KEY`
- Ensure no extra spaces or quotes around the key
- Restart terminal after setting environment variable
- Try entering key directly in web interface instead
- Verify key is copied correctly (no missing characters)

#### Problem: "Invalid API key" error

**Solution**:
- Verify key is correct - copy from API provider dashboard again
- Check if key has expired or been revoked
- Ensure you're using the right key for the right service
- Check API provider's dashboard for key status
- Generate a new API key if necessary

### Platform-Specific Issues

#### macOS Issues

**Problem**: "xcrun: error: invalid active developer path"

**Solution**:
```bash
xcode-select --install
```

**Problem**: Python version conflicts with system Python

**Solution**: Use Homebrew Python instead:
```bash
brew install python3
# Use full path or update PATH
```

#### Windows Issues

**Problem**: "Python was not found" in Command Prompt

**Solution**:
- Reinstall Python and check "Add Python to PATH"
- Or manually add Python to PATH in System Environment Variables
- Use PowerShell instead of Command Prompt

**Problem**: Script execution policy errors

**Solution**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Linux Issues

**Problem**: Missing development headers

**Solution**:
```bash
# Ubuntu/Debian
sudo apt-get install python3-dev build-essential

# Fedora
sudo dnf install python3-devel gcc
```

---

## Frequently Asked Questions (FAQ)

### General Questions

**Q: Do I need both Polygon and Alpha Vantage API keys?**  
A: No, you only need ONE data source API key. Choose based on your needs:
- **Alpha Vantage**: Free tier, good for beginners
- **Polygon**: Better for real-time features, paid plans available

**Q: Is xAI Grok required?**  
A: No, Grok is completely optional. The dashboard works fine without it, using keyword-based sentiment analysis instead.

**Q: Can I use this for commercial purposes?**  
A: Check the LICENSE file. Generally, this is open-source software, but verify the license terms for commercial use.

**Q: How much does it cost to run?**  
A: StockBro itself is free. Costs depend on API usage:
- **Alpha Vantage**: Free tier available (25 calls/day, 5 calls/minute)
- **Polygon**: Free tier with limitations, paid plans available
- **xAI Grok**: Per-token pricing (check x.ai/pricing)

**Q: Can I run this on a server for remote access?**  
A: Yes! Change `host='127.0.0.1'` to `host='0.0.0.0'` in `financial_dashboard.py`. Ensure proper security (firewall, authentication) for production use.

**Q: Does this work with mobile devices?**  
A: The web interface works on mobile browsers, but the experience is optimized for desktop. For mobile use, consider deploying to a server.

### Technical Questions

**Q: What Python version do I need?**  
A: Python 3.8 or higher. Python 3.10+ is recommended for best performance and compatibility.

**Q: Why use a virtual environment?**  
A: Virtual environments isolate dependencies, preventing conflicts with other Python projects and keeping your system Python clean.

**Q: Can I install without a virtual environment?**  
A: Yes, but it's not recommended. You can use `pip install -r requirements.txt` directly, but this may conflict with other Python packages.

**Q: How do I update StockBro to the latest version?**  
A: 
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

**Q: Can I customize the charts and indicators?**  
A: Yes! The code is open-source. Edit `financial_dashboard.py` to customize chart types, time periods, indicators, etc.

**Q: How do I add more technical indicators?**  
A: Add calculation functions (similar to `calculate_rsi`, `calculate_macd`) and create corresponding chart callbacks in the dashboard.

### API and Data Questions

**Q: Which API is better - Polygon or Alpha Vantage?**  
A: It depends on your needs:
- **Polygon**: Better for real-time data, WebSocket streaming, higher rate limits (paid)
- **Alpha Vantage**: Free tier, built-in sentiment analysis, good for casual use

**Q: How often does the data update?**  
A: 
- With auto-refresh enabled: Every 60 seconds
- Manual refresh: On button click
- WebSocket (Polygon): Real-time updates as they occur

**Q: Can I get data for international stocks?**  
A: Yes, if your API provider supports them. Check Polygon.io or Alpha Vantage documentation for supported markets and ticker formats.

**Q: Why am I getting rate limit errors?**  
A: You've exceeded your API provider's rate limits:
- **Alpha Vantage free tier**: 5 calls/minute, 25 calls/day
- **Polygon**: Varies by plan
- Solution: Wait between calls or upgrade your API plan

**Q: Is historical data stored locally?**  
A: No, StockBro doesn't store any data locally. All data is fetched fresh from APIs each time.

### Troubleshooting Questions

**Q: The dashboard won't start - what should I check?**  
A: 
1. Verify Python version: `python --version`
2. Check virtual environment is activated
3. Ensure all dependencies are installed: `pip list`
4. Check port 8050 is not in use
5. Verify no syntax errors: `python -m py_compile financial_dashboard.py`

**Q: Charts load but show no data**  
A: 
1. Verify API key is set correctly
2. Check ticker symbol is valid
3. Ensure internet connection is working
4. Check API service status
5. Try a different, well-known ticker (e.g., `AAPL`, `BTC-USD`)

**Q: I'm getting import errors**  
A: 
1. Ensure virtual environment is activated
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check Python version compatibility
4. Verify you're using the correct Python interpreter

**Q: The web page is blank**  
A: 
1. Check browser console (F12) for JavaScript errors
2. Verify internet connection (Plotly uses CDN)
3. Try a different browser
4. Clear browser cache
5. Check if Dash server is running (look for errors in terminal)

**Q: Can't connect to the dashboard from another device**  
A: 
1. Change `host='127.0.0.1'` to `host='0.0.0.0'` in the code
2. Check firewall settings
3. Verify both devices are on the same network
4. Use your computer's IP address: `http://YOUR_IP:8050`

### Feature Questions

**Q: Can I monitor multiple stocks at once?**  
A: Currently, StockBro monitors one asset at a time. You can switch between tickers using the refresh button. Multi-ticker support may be added in future versions.

**Q: Can I export data or charts?**  
A: Charts can be downloaded as PNG using the Plotly toolbar. Data export features may be added in future versions.

**Q: How accurate is the sentiment analysis?**  
A: Sentiment accuracy varies by method:
- **xAI Grok**: Most accurate, AI-powered with reasoning
- **Alpha Vantage**: Built-in AI sentiment, generally accurate
- **Keyword-based**: Basic but fast, good for general trends

**Q: Can I change the time period for historical data?**  
A: Currently fixed at 30 days. You can modify the `days=30` parameter in the `get_historical_data` function call to change this.

**Q: Does this support options or futures?**  
A: Currently supports stocks and cryptocurrencies only. Options and futures support depends on API provider capabilities.

### Security and Privacy Questions

**Q: Are my API keys secure?**  
A: Yes, when using environment variables. Keys are stored locally and never transmitted except to the API provider. Don't commit API keys to version control.

**Q: Is my data private?**  
A: Yes. All processing happens locally on your machine. Only API calls go to external services (Polygon, Alpha Vantage, xAI).

**Q: Can others access my dashboard?**  
A: By default, it only runs on localhost (`127.0.0.1`). If you change to `0.0.0.0` for network access, ensure proper firewall/security measures.

### Getting Help

**Q: Where can I get help?**  
A: 
- Check this README's Troubleshooting section
- Open an issue on [GitHub](https://github.com/seanebones-lang/stockbro)
- Check API provider documentation (Polygon.io, Alpha Vantage, xAI)

**Q: How do I report a bug?**  
A: Open an issue on GitHub with:
- Description of the problem
- Steps to reproduce
- Error messages (if any)
- Your system information (OS, Python version)
- What you've tried to fix it

**Q: Can I contribute to the project?**  
A: Yes! Contributions are welcome. See the Contributing section or open a pull request on GitHub.

---

## Usage

### Starting the Web Dashboard

Run the dashboard:
```bash
python financial_dashboard.py
```

Or use the convenience script:
```bash
./run_dashboard.sh
```

The dashboard will start a web server at `http://127.0.0.1:8050`. Open this URL in your web browser to access the interactive dashboard.

### Web Interface Features

The dashboard provides a user-friendly web interface with:

1. **Configuration Panel**:
   - **Asset Type**: Dropdown to select `stock` or `crypto`
   - **Ticker/Pair**: Text input for ticker symbol (e.g., `AAPL` for stocks, `BTC-USD` for crypto)
   - **Data Source**: Choose between `Polygon.io` or `Alpha Vantage`
   - **xAI Grok**: Toggle to enable Grok 4.1 Fast reasoning (requires XAI_API_KEY)
   - **Real-Time Updates**: Toggle for automatic refresh (Polygon only)
   - **Dark Mode**: Toggle between light and dark themes

2. **Data Visualization**:
   - **Statistics Summary**: Key metrics including current price, 30-day high/low, average price, and volume
   - **Historical Data Table**: Interactive table showing OHLCV data
   - **Price Chart**: Interactive Plotly chart with 7-day and 30-day moving averages
     - Hover for detailed values
     - Zoom and pan to explore specific periods
     - Download chart as PNG
   - **Candlestick Chart**: OHLC visualization with green/red candles
   - **Volume Chart**: Trading volume over time
   - **Technical Indicators**: RSI, MACD, and Bollinger Bands charts
   - **Recent News**: Latest articles with clickable links
   - **Sentiment Analysis**: Score and classification with color coding
   - **Latest Price**: Real-time or latest available price

3. **Auto-Refresh**: 
   - When "Real-Time Updates" is enabled, the dashboard automatically refreshes every 60 seconds
   - Manual refresh available via the "Refresh Dashboard" button

### Example Usage

1. **Start the server**:
   ```bash
   python financial_dashboard.py
   ```

2. **Open your browser** to `http://127.0.0.1:8050`

3. **Configure the dashboard**:
   - Select "Stock" or "Crypto" from Asset Type dropdown
   - Enter ticker symbol (e.g., `AAPL` for Apple stock, `BTC-USD` for Bitcoin)
   - Choose data source (Polygon or Alpha Vantage)
   - Enter your API key(s) or ensure they're set as environment variables
   - Optionally enable xAI Grok for advanced analysis
   - Enable real-time updates if using Polygon
   - Toggle dark mode for comfortable viewing

4. **Click "Refresh Dashboard"** to load data

5. **Interact with the charts**:
   - Hover over data points for detailed values
   - Use toolbar to zoom, pan, or download charts
   - Click and drag to zoom into specific time periods
   - Switch between light and dark modes

### Dashboard Components

The web dashboard displays:

- **📊 Statistics Summary**: Key metrics in an easy-to-read card layout
- **📈 Historical Data Table**: Interactive table with last 30 days of OHLCV data
  - Sortable columns
  - Scrollable for large datasets
- **📊 Price Chart**: Interactive Plotly line chart
  - Close price line (blue)
  - 7-day moving average (orange, dashed)
  - 30-day moving average (purple, dotted)
  - Hover tooltips with exact values
  - Zoom and pan controls
- **🕯️ Candlestick Chart**: OHLC visualization
  - Green candles for price increases
  - Red candles for price decreases
  - Full OHLC data visualization
- **📊 Volume Chart**: Trading volume bars
  - Visual representation of trading activity
  - Correlation with price movements
- **📊 Technical Indicators**:
  - **RSI**: Relative Strength Index with 70 (overbought) and 30 (oversold) markers
  - **MACD**: Moving Average Convergence Divergence with signal line and histogram
  - **Bollinger Bands**: Upper band, middle (SMA), and lower band with price overlay
- **📰 Recent News**: Latest articles
  - Titles and descriptions
  - Clickable "Read More" links
  - Publication dates
- **💭 Sentiment Analysis**: 
  - Color-coded sentiment (Green=Positive, Red=Negative, Gray=Neutral)
  - Score from -1 to 1
  - With Grok: Includes AI reasoning traces in console
- **💰 Latest Price**: Large, prominent display of current price

---

## API Key Setup

### Polygon.io (Massive)

1. Sign up at [massive.com](https://massive.com) (formerly polygon.io)
2. Get your API key from the dashboard
3. Free tier includes:
   - Limited REST API calls
   - Basic WebSocket streaming (rate-limited)
   - Historical data access
   - News feeds

For production use, consider upgrading to a paid plan for higher rate limits.

### Alpha Vantage

1. Sign up at [alphavantage.co](https://www.alphavantage.co/support/#api-key)
2. Get your free API key (instant access)
3. Free tier includes (as of 2025):
   - **25 API calls per day**
   - **5 API calls per minute** (rate limit)
   - Historical data (stocks and crypto)
   - News with built-in AI sentiment analysis
   - Real-time quotes (via polling)

**Important**: Alpha Vantage free tier has strict rate limits. The script automatically enforces a minimum 12-second interval between calls to respect the 5 calls/minute limit.

**Comparison**:
- **Polygon**: Better for real-time streaming, higher rate limits (paid tiers)
- **Alpha Vantage**: Free tier with built-in sentiment analysis, good for basic use cases

### xAI Grok 4.1 Fast (Optional)

1. Sign up at [x.ai/api](https://x.ai/api)
2. Get your API key from the dashboard
3. Free tier includes (as of December 2025):
   - Access to Grok 4.1 Fast reasoning model
   - Rate limits based on tier
   - 2M context window for deep analysis
   - Reasoning traces for transparency

**Features**:
- **Advanced Sentiment Analysis**: AI-powered sentiment with step-by-step reasoning
- **Market Insights**: Comprehensive analysis of trends and forecasts
- **Reasoning Effort Levels**: Choose between low, medium, or high for complexity
- **Reasoning Traces**: See how Grok arrives at conclusions

**Note**: Grok adds latency (TTFT ~1-2s in fast mode) and costs per token. Check [x.ai/pricing](https://x.ai/pricing) for details.

---

## Features in Detail

### Real-time Streaming
- Uses WebSocket connections for low-latency price updates (Polygon only)
- Automatically handles reconnections
- Thread-safe price updates using locks
- Separate subscriptions for stocks (`T.AAPL`) and crypto (`XT.BTC-USD`)

### Sentiment Analysis
- **xAI Grok 4.1 Fast** (if enabled): Advanced AI reasoning with step-by-step traces
  - Analyzes news context and provides reasoned sentiment scores
  - Returns classification with detailed reasoning
  - Configurable reasoning effort (low/medium/high)
  - Shows reasoning traces for transparency
- **Alpha Vantage**: Built-in AI sentiment scores from NEWS_SENTIMENT endpoint
  - Provides sentiment scores and labels per article
  - Overall sentiment aggregation
- **Polygon**: Keyword-based analysis (no external ML dependencies)
  - Analyzes news titles and descriptions
  - Returns sentiment score and classification
  - Expandable keyword lists for customization

### Historical Data
- Fetches daily aggregates (OHLCV)
- Configurable date ranges (30 days default)
- Displays in pandas DataFrame format
- Includes volume data

### Web Interface (Dash)
- Built with Dash (Plotly) - industry standard for Python web apps
- Interactive Plotly charts with zoom, pan, and hover
- Responsive design that works on desktop and tablet
- Real-time updates without page refresh
- Professional styling with color-coded components
- Dark mode support
- Download charts as PNG images

---

## Limitations & Notes

### Polygon.io
- **Rate Limits**: Free tier has rate limits; respect API guidelines
- **WebSocket**: Real-time streaming requires active WebSocket connection
- **News**: News availability depends on Polygon.io's coverage
- **Sentiment**: Keyword-based analysis (basic)

### Alpha Vantage
- **Rate Limits**: 
  - Free tier: 25 calls/day, 5 calls/minute
  - Script enforces minimum 12-second intervals
  - Consider upgrading for higher limits
- **WebSocket**: Not available in free tier; uses polling instead
- **News**: NEWS_SENTIMENT endpoint provides AI-powered sentiment scores
- **Crypto**: Supports major crypto pairs (BTC, ETH, etc.)
- **Real-time**: Uses polling (GLOBAL_QUOTE for stocks, CRYPTO_INTRADAY for crypto)

### xAI Grok
- **Latency**: Adds ~1-2 seconds per analysis (TTFT in fast mode)
- **Costs**: Per-token pricing; check x.ai/pricing for current rates
- **Rate Limits**: Based on your xAI tier; free tier has limits
- **Reasoning Traces**: Available for transparency; can be verbose

### General
- **Crypto Pairs**: Defaults to USD pairs; extend code for other currencies
- **Data Source**: Choose based on your needs (Polygon for real-time, Alpha Vantage for free tier with sentiment)
- **AI Enhancement**: Grok provides advanced analysis but is optional; falls back gracefully if unavailable

---

## Error Handling

The script includes comprehensive error handling for:
- API connection failures
- Invalid ticker symbols
- Missing data
- WebSocket disconnections
- Network timeouts
- Rate limit violations
- Invalid API keys
- Missing dependencies

---

## Compliance (2025 Standards)

- No persistent data storage (privacy-compliant)
- Environment variables for API keys (secure)
- Secure WebSocket connections (wss://)
- Minimal data retention
- Open-source code for transparency
- No tracking or analytics

---

## Contributing

Contributions are welcome! Areas for improvement:
- Additional technical indicators
- More data sources
- Export functionality (CSV, PNG)
- Multi-ticker monitoring
- Price alerts and notifications
- Mobile app version
- Additional chart types
- Performance optimizations

---

## License

See LICENSE file for details.

---

## Support

For issues with:
- **Polygon.io API**: Contact [Massive support](https://massive.com)
- **Alpha Vantage API**: Contact [Alpha Vantage support](https://www.alphavantage.co/support/)
- **xAI Grok API**: Contact [xAI support](https://x.ai/support) or check [x.ai/api](https://x.ai/api)
- **This Project**: Open an issue in the [GitHub repository](https://github.com/seanebones-lang/stockbro)

---

## Acknowledgments

- **Polygon.io (Massive)**: Market data and WebSocket streaming
- **Alpha Vantage**: Free-tier financial data and sentiment analysis
- **xAI**: Grok 4.1 Fast reasoning for advanced sentiment analysis
- **Dash (Plotly)**: Web framework and interactive visualizations
- **Pandas & NumPy**: Data processing and analysis

---

**Built with ❤️ for financial data enthusiasts**

*Empowering traders, investors, and researchers with accessible, professional-grade financial analysis tools.*
