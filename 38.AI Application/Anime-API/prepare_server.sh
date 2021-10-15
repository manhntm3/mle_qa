# apt-get update -y \
# && apt-get install -y \
apt-get install gunicorn 
# python3-dev \
# python3-pip \

python -m pip install -r requirements.txt

# rm -rf static
mkdir -p static
mkdir -p log
touch log/logger.log
