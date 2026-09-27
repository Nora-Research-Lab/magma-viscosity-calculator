FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV MPLBACKEND=Agg

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py magma_viscosity_calculator.py ./

EXPOSE 7860

CMD ["python", "app.py"]
