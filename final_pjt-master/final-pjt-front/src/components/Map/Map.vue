<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <br>
        <h1 class="text-center custom-text">주변 은행 검색</h1>
        <div class="input-group">
          <input type="text" @keyup.enter="search" placeholder="찾으시는 은행명 혹은 지역명을 입력하세요" v-model="searchKeyword" class="form-control">
          <div class="input-group-append">
            <button type="button" @click="search" class="btn custom-btn">검색</button>
          </div>
        </div>
      </div>
    </div>
    <div class="row justify-content-center mt-4">
      <div class="col-md-8">
        <div id="map" class="map-container"></div>
      </div>
    </div>
    <div class="row justify-content-center mt-4" v-if="bankList.length">
      <div class="col-md-8">
        <p class="mb-3 custom-text">근처에 총 {{ bankList.length }}개의 은행이 있습니다.</p>
        <hr class="custom-hr">
        <div v-for="(bank, index) in bankList" :key="bank.id" class="mb-3">
          <h5 class="custom-h5">[{{ index + 1 }}]</h5>
          <ul class="list-unstyled custom-list">
            <li><h4 class="custom-h4">{{ bank.place_name }}</h4></li>
            <li v-if="bank.phone"><strong class="custom-strong">전화번호 :</strong> {{ bank.phone }}</li>
            <li v-if="bank.road_address_name"><strong class="custom-strong">주소 :</strong> {{ bank.road_address_name }}</li>
            <li><a :href="bank.place_url" target="_blank" class="custom-link">[상세보기]</a></li>
          </ul>
          <hr class="custom-hr">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Map',
  data() {
    return {
      apiKey: this.$root.$data.apiKey,
      map:null,
      latitude:null,
      longitude:null,
      infowindow:null,
      basicControl: null,
      zoomControl: null,
      ps: null,
      bs: null,
      searchKeyword:null,
      bankList: []
    }
  },
  mounted() {
    this.apiKey = 'b95c5e19310025012cecb21ea0dc5e1f'

    const script = document.createElement('script');
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${this.apiKey}&autoload=false`
    const scriptForLib = document.createElement('script');
    scriptForLib.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${this.apiKey}&libraries=services,clusterer,drawing&autoload=false`
    script.onload = () => {
      kakao.maps.load(this.fetchLocation)
    }
    document.body.appendChild(script);
    document.body.appendChild(scriptForLib);
  },
  methods: {
    fetchLocation() {
      const compo = this

      const options = {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0,
      };

      function success(pos) {
        const crd = pos.coords;

        compo.latitude = crd.latitude;
        compo.longitude = crd.longitude;
        compo.createMap()
      }

      function error(err) {
        console.warn(`ERROR(${err.code}): ${err.message}`);
      }

      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success, error, options);
      } else {
        alert("이 브라우저에서는 Geolocation이 지원되지 않습니다.");
      }
    },
    createMap() {
      const container = document.getElementById('map');
      const options = {
        center: new kakao.maps.LatLng(this.latitude, this.longitude),
        level: 5
      };

      this.map = new kakao.maps.Map(container, options);
      this.bs = new kakao.maps.services.Places(this.map);
      this.basicControl = new kakao.maps.MapTypeControl();
      this.zoomControl = new kakao.maps.ZoomControl();

      this.map.addControl(this.basicControl, kakao.maps.ControlPosition.TOPRIGHT);
      this.map.addControl(this.zoomControl, kakao.maps.ControlPosition.RIGHT);
      const compo = this
      const kakaoo = kakao.maps

      function placeSearchCB(data, status, pagination) {
        if (status == kakaoo.services.Status.OK) {

          for (var i = 0; i < data.length; i++) {
            compo.displayMarker(data[i]);

          }
        }
      }
      this.bs.categorySearch('BK9',placeSearchCB,{useMapBounds:true})
    },
    search() {
      this.ps = new kakao.maps.services.Places();
      
      const compo = this
      const kakaoo = kakao.maps
      

      function placeSearchCB(data, status, pagination) {
        if (status == kakaoo.services.Status.OK) {
         
          var bounds = new kakao.maps.LatLngBounds();
          for (var i = 0; i < data.length; i++) {
            
            if (data[i].category_group_code == 'BK9') {
            compo.bankList.push(data[i])
          }
        
            compo.displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
          }
        compo.map.setBounds(bounds);
        
        }
      }

      this.ps.keywordSearch(this.searchKeyword,placeSearchCB)
      this.bankList=[]

    },
    displayMarker(place) {
      const compo = this
      this.infowindow = new kakao.maps.InfoWindow({zIndex:1});
      const marker = new kakao.maps.Marker({
        map: this.map,
        position: new kakao.maps.LatLng(place.y, place.x)
      })
      kakao.maps.event.addListener(marker, 'click', function() {
        compo.infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        compo.infowindow.open(compo.map, marker);
      })
    },
  }
}
</script>


<style scoped>
#map {
  width: 100%; 
  height: 400px;
  margin-bottom: 30px;
}

.map-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.input-group {
  margin-bottom: 20px;
}

.input-group-append button {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.input-group-append button:hover {
  background-color: #28a745;
  color: white;
}

.list-unstyled {
  padding-left: 0;
  list-style: none;
}

.list-unstyled li {
  margin-bottom: 5px;
}

.custom-text {
  color: #343a40;
}

.custom-hr {
  border-top: 1px solid #dee2e6;
}

.custom-h5 {
  color: #007bff;
}

.custom-h4 {
  color: #6c757d;
}

.custom-strong {
  margin-right: 5px;
}

.custom-link {
  color: #007bff;
  text-decoration: none;
}

.custom-link:hover {
  text-decoration: underline;
}
</style>