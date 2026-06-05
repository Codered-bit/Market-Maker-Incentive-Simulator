# Market-Maker-Incentive-Simulator
simulator that dynamically adjusts incentive weights, ranks market makers by liquidity contribution, and allocates rewards proportionally while monitoring operational risk through automated alerts.
# Market Maker Performance & Incentive Simulator

## Overview

The Market Maker Performance & Incentive Simulator is a liquidity operations dashboard designed to evaluate market maker performance, simulate incentive distribution programs, and monitor operational risks.

The project models how a decentralized trading venue might assess liquidity providers, allocate rewards, and identify performance issues through data-driven analytics.

Built with Python and Streamlit, the dashboard provides an interactive environment for testing incentive structures and evaluating market maker behaviour.

---

## Business Problem

Liquidity is one of the most critical components of any trading venue.

Exchanges and trading protocols often incentivize market makers to:

- Provide consistent liquidity
- Maintain tight spreads
- Achieve high uptime
- Support healthy trading activity

The challenge is determining:

- How performance should be measured
- How incentives should be distributed fairly
- How operational issues should be detected and monitored

This project provides a framework for addressing these challenges.

---

## Features

### Liquidity Performance Scoring

Each market maker receives a composite Liquidity Score based on:

- Trading Volume
- Order Activity
- Uptime
- Spread Competitiveness

The scoring methodology can be customized through adjustable weighting parameters.

---

### Incentive Distribution Engine

The dashboard simulates reward allocation from a configurable incentive pool.

Rewards are distributed proportionally according to each participant's liquidity contribution.

---

### Dynamic Weight Simulation

Users can adjust the importance of:

- Volume
- Orders
- Uptime
- Spread Quality

and instantly observe how rankings and reward allocations change.

This feature demonstrates incentive mechanism design and testing.

---

### Leaderboard System

Market makers are ranked according to their Liquidity Scores.

The leaderboard highlights:

- Top-performing liquidity providers
- Relative performance differences
- Incentive eligibility

---

### Operational Alert Center

The dashboard automatically flags:

- Excessive spreads
- Low uptime
- Significant volume declines

These alerts help identify participants requiring operational review.

---

### Executive Summary Generation

The application generates an automated management summary describing:

- Top-performing market makers
- Reward allocation outcomes
- Active operational risks
- Key program observations

---

## Methodology

### Liquidity Score Framework

The liquidity score is calculated using a weighted combination of:

- Volume Score
- Order Activity Score
- Uptime Score
- Spread Score

General form:

Liquidity Score =

(Volume Weight × Volume Score)

+ (Order Weight × Order Score)

+ (Uptime Weight × Uptime Score)

+ (Spread Weight × Spread Score)

Higher scores indicate stronger overall liquidity contribution.

---

### Reward Allocation

Incentives are distributed proportionally:

Reward Allocation =

(Market Maker Liquidity Score ÷ Total Liquidity Scores)

× Reward Pool

This ensures rewards remain aligned with performance.

---

### Alert Detection Rules

Operational alerts are generated when:

- Spread exceeds defined thresholds
- Uptime falls below acceptable levels
- Trading volume drops significantly

---

## Dashboard Components

### Liquidity Operations Overview

Displays:

- Number of Market Makers
- Total Reward Pool
- Average Liquidity Score
- Active Alerts

### Liquidity Leaderboard

Ranks market makers by performance.

### Incentive Allocation Dashboard

Visualizes reward distribution across participants.

### Alert Center

Displays operational warnings and exceptions.

### Executive Summary

Provides management-level insights.

---

## Technology Stack

- Python
- Streamlit
- Pandas
- NumPy

---

## Project Structure

```text
.
├── app.py
├── requirements.txt
└── README.md
```

---

## Example Use Cases

This framework can be extended for:

- Liquidity operations monitoring
- Market maker evaluation
- Incentive program design
- DeFi protocol analytics
- Exchange operations
- Trading venue performance management

---

## Future Enhancements

Planned improvements include:

- Historical performance tracking
- Real market data integration
- Multi-market simulations
- Market maker segmentation
- Liquidity mining analytics
- Advanced anomaly detection
- Machine learning-based performance forecasting

---

## Key Skills Demonstrated

- Data Analysis
- Liquidity Analytics
- Market Structure Analysis
- Incentive Design
- KPI Development
- Dashboard Development
- Operational Monitoring
- Statistical Analysis

---

## About the Author

**Dare Shonubi**

- MSc Financial Technology & Trading
- BSc Data Science
- BSc Business Administration
- Google Data Analytics Professional Certificate
- Blockchain & Cryptocurrency Certifications

This project was developed as part of a portfolio focused on cryptocurrency markets, liquidity analytics, trading operations, and decentralized finance infrastructure.
