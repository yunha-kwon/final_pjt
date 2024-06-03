<template>
  <div>
    <!-- Carousel -->
    <div id="carouselExampleIndicators" class="carousel slide custom-carousel animate__animated animate__fadeIn" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="parallax-container">
            <img src="@/assets/result_rich2.png" class="d-block w-100" alt="Welcome">
            <div class="parallax-content animate__animated animate__fadeInUp">
              <h4>안전하고 신뢰성있는 금융 서비스</h4>
            </div>
          </div>
        </div>
        <div class="carousel-item">
          <img src="@/assets/result_second.jpg" class="d-block w-100 animate__animated animate__fadeIn" alt="Services">
        </div>
        <div class="carousel-item">
          <img src="@/assets/result_lulu.jpg" class="d-block w-100 animate__animated animate__fadeIn" alt="Support">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>

    <!-- Cards -->
    <div class="container mt-5 mb-5">
      <div class="row">
        <div class="col-md-4 mb-4 animate__animated animate__zoomIn">
          <div class="card">
            <img src="@/assets/gogo.jpg" class="card-img-top" alt="Online Banking">
            <div class="card-body">
              <h2 class="card-title">정기 예금 상품</h2>
              <p class="card-text">2030 청년들을 위한 정기예금이 궁금하다면?</p>
              <a href="/products" class="btn btn-primary">Learn More</a>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4 animate__animated animate__zoomIn" style="animation-delay: 0.2s;">
          <div class="card">
            <img src="@/assets/select.jpg" class="card-img-top" alt="Loans">
            <div class="card-body">
              <h5 class="card-title">금융 상품 추천</h5>
              <p class="card-text">나에게 딱 맞는 금융 상품을 찾아보세요!</p>
              <a href="/personal" class="btn btn-primary">Learn More</a>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4 animate__animated animate__zoomIn" style="animation-delay: 0.4s;">
          <div class="card">
            <img src="@/assets/last.jpg" class="card-img-top" alt="Support">
            <div class="card-body">
              <h5 class="card-title">Y&S 자유 게시판</h5>
              <p class="card-text">금융 관련 정보를 확인하고 자유롭게 소통해보세요!</p>
              <a href="/articles" class="btn btn-primary">Contact Us</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import 'animate.css';
</script>

<style scoped>
.custom-carousel {
  max-height: 400px;
  overflow: hidden;
}

.card-title {
  font-size: 19px;
}

.carousel-inner img {
  height: 400px;
  object-fit: cover;
}

.mb-4 {
  margin-bottom: 1.5rem;
}

.parallax-container {
  position: relative;
  height: 400px;
}

.parallax-content {
  position: absolute;
  top: 85%;
  left: 42%;
  transform: translate(-50%, -50%);
  color: #fff;
  text-align: center;
}
</style>