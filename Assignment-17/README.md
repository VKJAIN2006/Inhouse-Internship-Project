Build Docker Image
docker build -t sales-analysis .

Run Container
docker run --name sales-container sales-analysis

Output

Filtered products are saved in:
output/high_sales_products
output/sorted_products
output/top3_products