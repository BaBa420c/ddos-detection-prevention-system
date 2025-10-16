from flask import Flask, render_template, request, jsonify
import redis
import time
import logging
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
    redis_client.ping()
    logger.info("Connected to Redis successfully")
except Exception as e:
    logger.error(f"Redis connection failed: {e}")
    redis_client = None

request_count = 0
start_time = time.time()

@app.route('/')
def index():
    global request_count
    request_count += 1
    
    client_ip = request.remote_addr
    timestamp = datetime.now().isoformat()
    
    if redis_client:
        try:
            redis_client.incr(f"request_count:{client_ip}")
            redis_client.lpush("recent_requests", f"{timestamp}|{client_ip}")
            redis_client.ltrim("recent_requests", 0, 999)
        except Exception as e:
            logger.error(f"Redis error: {e}")
    
    return render_template('index.html', request_count=request_count, uptime=int(time.time() - start_time))

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'healthy',
        'uptime': int(time.time() - start_time),
        'total_requests': request_count,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/metrics')
def metrics():
    uptime = int(time.time() - start_time)
    metrics_text = f"""# HELP http_requests_total Total HTTP requests
# TYPE http_requests_total counter
http_requests_total {request_count}

# HELP http_server_uptime_seconds Server uptime in seconds
# TYPE http_server_uptime_seconds gauge
http_server_uptime_seconds {uptime}
"""
    return metrics_text, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
