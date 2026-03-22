# Casino Bot

## Features
- User-friendly interface for managing casino games.
- Supports multiple game types: blackjack, roulette, slots, etc.
- Payout management for all games.
- Customizable game rules and settings.
- Logging and analytics of user activities.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hash20896-coder/casino-bot.git
   ```
2. Navigate into the project directory:
   ```bash
   cd casino-bot
   ```
3. Install the required dependencies:
   ```bash
   npm install
   ```

## Setup
1. Create a `.env` file based on the `.env.example` file in the root directory.
2. Configure your database connection and any necessary API keys.
3. Run the initial migration to set up your database:
   ```bash
   npm run migrate
   ```

## Commands
- **Start the Bot**:
   ```bash
   npm start
   ```
- **Show Help**:
   ```bash
   npm run help
   ```
- **Custom Command**:
   ```bash
   npm run custom-command
   ```

## Game Payouts
### Blackjack
- Winning: 1.5x the bet
- Losing: 0x the bet

### Roulette
- Winning on number: 35x the bet
- Winning on color: 2x the bet

### Slots
- Payout varies depending on the combination:
  - Three of a kind: 10x the bet
  - Two of a kind: 2x the bet

## Troubleshooting
- **Bot won't start**: Check if all dependencies are installed correctly and review the console for error messages.
- **Database connection issues**: Ensure your database is running and credentials in the `.env` file are correct.
- **Unexpected behaviors**: Review the logs in the `logs/` directory for any warnings or errors.

## Contact
For further assistance, you can reach out to hash20896-coder on GitHub or create an issue in this repository.