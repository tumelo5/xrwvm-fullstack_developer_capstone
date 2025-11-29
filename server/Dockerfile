# 1. Base image
FROM python:3.12.0-slim-bookworm

# 2. Environment variables
ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
ENV APP=/app

# 3. Change working directory
WORKDIR $APP

# 4. Add requirements file
COPY requirements.txt $APP/

# 5. Install and update Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6. Copy the rest of your app
COPY . $APP/

# Make entrypoint executable (only if you have entrypoint.sh)
RUN chmod +x /app/entrypoint.sh

# 7. Expose port for Django
EXPOSE 8000

# 8. Start the application
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
