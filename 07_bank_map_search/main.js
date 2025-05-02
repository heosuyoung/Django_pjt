let map;
let markers = [];
let polyline;

const START_LAT = 37.5012743;   // 멀티캠퍼스 역삼
const START_LNG = 127.039585;

function loadKakaoMapScript(callback) {
  const script = document.createElement('script');
  script.onload = callback;
  script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${KAKAO_API_KEY}&autoload=false&libraries=services`;
  document.head.appendChild(script);
}

window.onload = function () {
  loadKakaoMapScript(() => {
    kakao.maps.load(() => {
      initializeMap();
      populateSido();
    });
  });
};

function initializeMap() {
  const container = document.getElementById('map');
  const options = {
    center: new kakao.maps.LatLng(START_LAT, START_LNG),
    level: 5
  };
  map = new kakao.maps.Map(container, options);

  // ✅ 출발지 마커 추가 (START_LAT, START_LNG 기준)
  // ✅ 출발지 마커 (파란색)
  const startMarker = new kakao.maps.Marker({
    position: new kakao.maps.LatLng(START_LAT, START_LNG),
    map: map,
    title: "출발지",
    image: new kakao.maps.MarkerImage(
      "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png", // 예시 이미지
      new kakao.maps.Size(24, 35)
    )
  });
  
  
}

function populateSido() {
  const sidoSelect = document.getElementById('sido');
  sidoSelect.innerHTML = `<option value="">광역시/도 선택</option>`;

  for (let sido in locationData) {
    const option = document.createElement('option');
    option.value = sido;
    option.textContent = sido;
    sidoSelect.appendChild(option);
  }

  sidoSelect.addEventListener('change', populateSigungu);
}

function populateSigungu() {
  const sido = document.getElementById('sido').value;
  const sigunguSelect = document.getElementById('sigungu');
  const bankSelect = document.getElementById('bank');
  sigunguSelect.innerHTML = `<option value="">시/군/구 선택</option>`;
  bankSelect.innerHTML = `<option value="">은행 선택</option>`;

  if (!sido) return;

  for (let sigungu in locationData[sido]) {
    const option = document.createElement('option');
    option.value = sigungu;
    option.textContent = sigungu;
    sigunguSelect.appendChild(option);
  }

  sigunguSelect.addEventListener('change', populateBank);
}

function populateBank() {
  const sido = document.getElementById('sido').value;
  const sigungu = document.getElementById('sigungu').value;
  const bankSelect = document.getElementById('bank');
  bankSelect.innerHTML = `<option value="">은행 선택</option>`;

  if (!sido || !sigungu) return;

  const banks = locationData[sido][sigungu];
  for (let bank of banks) {
    const option = document.createElement('option');
    option.value = bank;
    option.textContent = bank;
    bankSelect.appendChild(option);
  }
}

function clearMarkers() {
  for (let marker of markers) {
    marker.setMap(null);
  }
  markers = [];

  if (polyline) {
    polyline.setMap(null);
    polyline = null;
  }
}

function searchBanks() {
  const sido = document.getElementById('sido').value;
  const sigungu = document.getElementById('sigungu').value;
  const bank = document.getElementById('bank').value;

  if (!sido || !sigungu || !bank) {
    alert("모든 항목을 선택하세요.");
    return;
  }

  const keyword = `${sido} ${sigungu} ${bank}`;
  const ps = new kakao.maps.services.Places();

  clearMarkers();

  ps.keywordSearch(keyword, function (results, status) {
    if (status === kakao.maps.services.Status.OK) {
      const bounds = new kakao.maps.LatLngBounds();

      results.forEach((place) => {
        const position = new kakao.maps.LatLng(place.y, place.x);

        const marker = new kakao.maps.Marker({
          map,
          position
        });

        const infowindow = new kakao.maps.InfoWindow({
          content: `<div style="padding:5px;">${place.place_name}</div>`
        });

        marker.addListener('click', () => {
          infowindow.open(map, marker);
          drawRoute(place.y, place.x);  // 경로 표시 추가
        });

        markers.push(marker);
        bounds.extend(position);
      });

      map.setBounds(bounds);
    } else {
      alert("검색 결과가 없습니다.");
    }
  });
}

// ✅ 경로 그리기 함수
function drawRoute(destLat, destLng) {
    if (polyline) {
      polyline.setMap(null);
    }
  
    const proxy = "https://cors-anywhere.herokuapp.com/";
    const url = `${proxy}https://apis-navi.kakaomobility.com/v1/directions?origin=${START_LNG},${START_LAT}&destination=${destLng},${destLat}&priority=RECOMMEND`;
  
    fetch(url, {
      method: "GET",
      headers: {
        Authorization: `KakaoAK ${KAKAO_MOBILITY_KEY}`
      }
    })
      .then(res => res.json())
      .then(data => {
        console.log("🟡 응답 데이터:", data);
  
        // ✅ 경로 없음 처리
        const roads = data?.routes?.[0]?.sections?.[0]?.roads;
        if (!roads || roads.length === 0) {
          alert("🚫 해당 위치는 자동차 경로를 찾을 수 없습니다.");
          return;
        }
  
        // ✅ 좌표 리스트 변환
        const coords = roads.flatMap(road =>
          road.vertexes.reduce((acc, val, idx, arr) => {
            if (idx % 2 === 0) {
              acc.push(new kakao.maps.LatLng(arr[idx + 1], val));
            }
            return acc;
          }, [])
        );
  
        if (!coords || coords.length === 0) {
          alert("⚠️ 경로 좌표 생성에 실패했습니다.");
          return;
        }
  
        // ✅ 선 그리기
        polyline = new kakao.maps.Polyline({
          map: map,
          path: coords,
          strokeWeight: 4,
          strokeColor: '#FF6600',
          strokeOpacity: 0.9,
          strokeStyle: 'solid'
        });
  
        // ✅ 지도 범위 자동 조정
        if (typeof polyline.getBounds === "function") {
          map.setBounds(polyline.getBounds());
        } else {
          console.warn("⚠️ polyline.getBounds is not a function");
        }
      })
      .catch(err => {
        alert("❌ 경로를 불러오는 데 실패했습니다.");
        console.error("🔥 fetch 실패 이유:", err);
      });
  }
  
  