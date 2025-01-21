# openlit-demo


#### Start openlit server using docker compose:
```shell
cd openlit-docker
docker compose up -d 
# Open browser: 
  http://localhost:3000/
  username - user@openlit.io
  password - openlituser
```

#### Ollama setup on local:
```shell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

docker exec -it ollama ollama run llama3.1
```

### Start openlit demo app:
```shell
poetry config virtualenvs.in-project true
poetry install
python main.py
### API docs
http://localhost:8000/docs
```

#### Test using curl request:
```shell
curl --location 'http://localhost:8000/v1/api/chat' \
--header 'Content-Type: application/json' \
--data '{
  "model": "llama3",
  "question": "Tell me about Nvidia'\''s Future?"
}'
#### response:
{
    "answer": "NVIDIA is a leading technology company that has been at the forefront of innovation in various fields, including graphics processing units (GPUs), high-performance computing, artificial intelligence (AI), and autonomous vehicles. Here are some potential future developments and trends related to NVIDIA:\n\n**Short-term (2023-2025)**\n\n1. **Advancements in AI**: NVIDIA will continue to push the boundaries of AI research and development, with a focus on areas like natural language processing, computer vision, and reinforcement learning.\n2. **Increased adoption of GPUs for HPC**: As high-performance computing (HPC) becomes more widespread, NVIDIA's GPUs are expected to play an increasingly important role in accelerating simulations, modeling, and data analysis.\n3. **Expansion of autonomous vehicle technology**: NVIDIA will continue to develop its Drive platform, which enables the development of Level 2-5 autonomous vehicles.\n\n**Mid-term (2025-2030)**\n\n1. **Quantum Computing**: NVIDIA is exploring the potential of quantum computing and has already demonstrated a proof-of-concept for a quantum-accelerated GPU.\n2. **Advancements in Edge AI**: As edge computing becomes more prevalent, NVIDIA will focus on developing more efficient and powerful edge AI solutions that can be deployed at the edge of networks.\n3. **Increased adoption of GPUs in data centers**: With the growing demand for cloud services, NVIDIA's GPUs are expected to become even more ubiquitous in data centers.\n\n**Long-term (2030-2040)**\n\n1. **Neuromorphic Computing**: NVIDIA is researching neuromorphic computing architectures that mimic the human brain's neural networks. This could lead to significant breakthroughs in AI and machine learning.\n2. **Advancements in 3D XPoint Technology**: NVIDIA has acquired a company called Bright, which specializes in 3D XPoint technology (a type of non-volatile memory). This could enable faster and more efficient data storage solutions.\n3. **Increased focus on sustainability**: As the world becomes increasingly aware of environmental concerns, NVIDIA may prioritize developing more energy-efficient and sustainable technologies.\n\n**Speculative Future Developments**\n\n1. **Brain-Computer Interfaces (BCIs)**: NVIDIA has already demonstrated a BCI prototype that enables people to control devices with their thoughts.\n2. **Quantum-Accelerated AI**: As quantum computing advances, it's possible that NVIDIA will develop quantum-accelerated AI solutions that can solve complex problems in fields like medicine and climate modeling.\n3. **Holographic Displays**: With the development of advanced display technologies, NVIDIA may explore the creation of holographic displays that enable immersive experiences.\n\nKeep in mind that these are just predictions based on current trends and NVIDIA's past innovations. The future is inherently uncertain, and actual developments may differ from these projections."
}
```