from app.data.models import ProvinceOrCity

class ProvinceAndCityService:
    @staticmethod
    def read_all() -> list[ProvinceOrCity]:
        return [
            ProvinceOrCity(12370,"01","Thành phố Hà Nội",1),
            ProvinceOrCity(12371,"04","Tỉnh Cao Bằng",1),
            ProvinceOrCity(12372,"08","Tỉnh Tuyên Quang",1),
            ProvinceOrCity(12373,"11","Tỉnh Điện Biên",1),
            ProvinceOrCity(12374,"12","Tỉnh Lai Châu",1),
            ProvinceOrCity(12375,"14","Tỉnh Sơn La",1),
            ProvinceOrCity(12376,"15","Tỉnh Lào Cai",1),
            ProvinceOrCity(12377,"19","Tỉnh Thái Nguyên",1),
            ProvinceOrCity(12378,"20","Tỉnh Lạng Sơn",1),
            ProvinceOrCity(12379,"22","Tỉnh Quảng Ninh",1),
            ProvinceOrCity(12380,"24","Tỉnh Bắc Ninh",1),
            ProvinceOrCity(12381,"25","Tỉnh Phú Thọ",1),
            ProvinceOrCity(12382,"31","Thành phố Hải Phòng",1),
            ProvinceOrCity(12383,"33","Tỉnh Hưng Yên",1),
            ProvinceOrCity(12384,"37","Tỉnh Ninh Bình",1),
            ProvinceOrCity(12385,"38","Tỉnh Thanh Hóa",1),
            ProvinceOrCity(12386,"40","Tỉnh Nghệ An",1),
            ProvinceOrCity(12387,"42","Tỉnh Hà Tĩnh",1),
            ProvinceOrCity(12388,"44","Tỉnh Quảng Trị",1),
            ProvinceOrCity(12389,"46","Thành phố Huế",1),
            ProvinceOrCity(12390,"48","Thành phố Đà Nẵng",1),
            ProvinceOrCity(12391,"51","Tỉnh Quảng Ngãi",1),
            ProvinceOrCity(12392,"52","Tỉnh Gia Lai",1),
            ProvinceOrCity(12393,"56","Tỉnh Khánh Hòa",1),
            ProvinceOrCity(12394,"66","Tỉnh Đắk Lắk",1),
            ProvinceOrCity(12395,"68","Tỉnh Lâm Đồng",1),
            ProvinceOrCity(12396,"75","Tỉnh Đồng Nai",1),
            ProvinceOrCity(12397,"79","Thành phố Hồ Chí Minh",1),
            ProvinceOrCity(12398,"80","Tỉnh Tây Ninh",1),
            ProvinceOrCity(12399,"82","Tỉnh Đồng Tháp",1),
            ProvinceOrCity(12400,"86","Tỉnh Vĩnh Long",1),
            ProvinceOrCity(12401,"91","Tỉnh An Giang",1),
            ProvinceOrCity(12402,"92","Thành phố Cần Thơ",1),
            ProvinceOrCity(12403,"96","Tỉnh Cà Mau",1)
        ]