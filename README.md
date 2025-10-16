# DDoS Detection and Prevention System in Simulated Cloud Network

[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 📋 Project Overview

This project implements a comprehensive DDoS (Distributed Denial of Service) detection and prevention system in a simulated cloud network environment. It demonstrates various attack types, real-time detection algorithms, and automatic mitigation strategies.

**Perfect for**: Computer Science projects, Security demonstrations, Educational purposes

## ✨ Features

- **Multiple Attack Types**:
  - SYN Flood Attack
  - HTTP GET/POST Flood
  - Slowloris Attack
  - UDP Flood Attack

- **Real-time Detection**:
  - Statistical anomaly detection
  - Rate-based detection
  - Pattern recognition
  - Machine Learning classification

- **Automatic Prevention**:
  - Dynamic IP blacklisting
  - Rate limiting
  - Connection throttling
  - Geographic filtering

- **Monitoring & Visualization**:
  - Real-time metrics dashboard
  - Attack timeline visualization
  - Traffic analysis graphs
  - Alert system

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Docker Network                          │
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐ │
│  │   Attacker   │───▶│   Firewall   │───▶│  Web Server  │ │
│  │  (Simulator) │    │     (WAF)    │    │   (Flask)    │ │
│  └──────────────┘    └──────────────┘    └──────────────┘ │
│         │                    │                    │         │
│         │                    ▼                    │         │
│         │            ┌──────────────┐            │         │
│         └───────────▶│   Detector   │◀───────────┘         │
│                      │     (IDS)    │                      │
│                      └──────────────┘                      │
│                             │                              │
│                             ▼                              │
│                      ┌──────────────┐                      │
│                      │  Prometheus  │                      │
│                      │   + Grafana  │                      │
│                      └──────────────┘                      │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Docker** & **Docker Compose** installed
- **16GB RAM** recommended (8GB minimum)
- **10GB free disk space**
- **Python 3.10+** (for local development)

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/BaBa420c/ddos-detection-prevention-system.git
cd ddos-detection-prevention-system
```

2. **Run setup script**:
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

3. **Start all services**:
```bash
docker-compose up -d
```

4. **Access the dashboard**:
- **Web Server**: http://localhost:5000
- **Grafana Dashboard**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9090

## 🎯 Demo Instructions

### 1. Normal Traffic Test
```bash
curl http://localhost:5000
```

### 2. Launch SYN Flood Attack
```bash
docker-compose exec attacker python syn_flood.py
```

### 3. Launch HTTP Flood Attack
```bash
docker-compose exec attacker python http_flood.py
```

### 4. Launch Slowloris Attack
```bash
docker-compose exec attacker python slowloris.py
```

### 5. View Real-time Detection
- Open Grafana: http://localhost:3000
- Check alerts and blocked IPs
- Monitor traffic graphs

### 6. Stop All Attacks
```bash
./scripts/stop_attack.sh
```

## 📁 Project Structure

```
ddos-detection-prevention-system/
├── docker-compose.yml           # Docker orchestration
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
│
├── docs/                        # Documentation
│   ├── architecture.md          # System architecture
│   ├── attack-types.md          # Attack descriptions
│   └── screenshots/             # Demo screenshots
│
├── src/
│   ├── web_server/              # Target web application
│   │   ├── Dockerfile
│   │   ├── app.py               # Flask server
│   │   ├── requirements.txt
│   │   └── templates/
│   │       └── index.html
│   │
│   ├── attacker/                # Attack simulators
│   │   ├── Dockerfile
│   │   ├── syn_flood.py         # SYN flood attack
│   │   ├── http_flood.py        # HTTP flood attack
│   │   ├── slowloris.py         # Slowloris attack
│   │   ├── udp_flood.py         # UDP flood attack
│   │   └── requirements.txt
│   │
│   ├── detector/                # IDS system
│   │   ├── Dockerfile
│   │   ├── ids.py               # Main detection logic
│   │   ├── anomaly_detection.py # ML-based detection
│   │   ├── rate_limiter.py      # Rate limiting
│   │   └── requirements.txt
│   │
│   ├── firewall/                # WAF system
│   │   ├── Dockerfile
│   │   ├── waf.py               # Web Application Firewall
│   │   ├── rules.json           # Firewall rules
│   │   └── requirements.txt
│   │
│   └── monitor/                 # Monitoring system
│       ├── dashboard.py         # Metrics collector
│       ├── prometheus.yml       # Prometheus config
│       └── grafana-dashboard.json
│
├── scripts/                     # Utility scripts
│   ├── setup.sh                 # Initial setup
│   ├── run_attack.sh            # Run attack scenarios
│   ├── stop_attack.sh           # Stop all attacks
│   └── cleanup.sh               # Clean up resources
│
└── tests/                       # Test suite
    ├── test_detection.py
    ├── test_prevention.py
    └── test_attacks.py
```

## 🔧 Technologies Used

| Component | Technology |
|-----------|-----------|
| **Containerization** | Docker, Docker Compose |
| **Web Server** | Flask, Nginx |
| **Programming** | Python 3.10+ |
| **Attack Simulation** | Scapy, Requests, Socket |
| **Detection** | scikit-learn, pandas, numpy |
| **Monitoring** | Prometheus, Grafana |
| **Caching/Rate Limiting** | Redis |
| **Data Storage** | SQLite, Elasticsearch |

## 💻 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 8GB | 16GB DDR5 ✅ |
| **CPU** | 4 cores | 8 cores |
| **Storage** | 10GB | 20GB NVMe ✅ |
| **GPU** | Not required | RTX 4060 (Optional) |

**Your System**: Perfect for this project! ✅

## 📊 Metrics & Monitoring

The system tracks:
- **Requests per second**
- **Connection count**
- **Packet drop rate**
- **CPU/Memory usage**
- **Attack detection rate**
- **False positive rate**
- **Blocked IPs count**
- **Response time**

## 🛡️ Safety Features

- ✅ **Isolated Docker network** - No external traffic
- ✅ **Resource limits** - CPU & RAM caps
- ✅ **Auto-stop timers** - Prevents runaway attacks
- ✅ **Emergency shutdown** - Ctrl+C stops everything
- ✅ **No real targets** - Everything runs locally

## 📖 Documentation

- [Architecture Design](docs/architecture.md)
- [Attack Types Explained](docs/attack-types.md)
- [Detection Algorithms](docs/detection-algorithms.md)
- [API Reference](docs/api-reference.md)

## 🎓 Educational Use

This project is designed for:
- Computer Science final year projects
- Cybersecurity courses
- Network security demonstrations
- Cloud computing labs
- Research purposes

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**BaBa420c**
- GitHub: [@BaBa420c](https://github.com/BaBa420c)

## 🙏 Acknowledgments

- Docker Community
- Flask Framework
- Prometheus & Grafana Teams
- Open Source Security Community

## 📞 Support

If you have questions or need help:
- Open an [Issue](https://github.com/BaBa420c/ddos-detection-prevention-system/issues)
- Check the [Documentation](docs/)

## ⭐ Star this repository if you find it helpful!

---

**Made with ❤️ for Computer Science Education**