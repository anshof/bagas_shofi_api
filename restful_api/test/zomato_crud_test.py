import json
from . import app, client, cache, create_token, init_database
from unittest import mock
from unittest.mock import patch

class TestZomatoCrud():

    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
            
            def json(self):
                return self.json_data

        if len(args) > 0:
            if args[0] == app.config['ZO_HOST'] + "/cities":
                return MockResponse({
  "location_suggestions": [
    {
      "id": 74,
      "name": "Jakarta",
      "country_id": 94,
      "country_name": "Indonesia",
      "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_94.png",
      "should_experiment_with": 0,
      "has_go_out_tab": 0,
      "discovery_enabled": 0,
      "has_new_ad_format": 1,
      "is_state": 0,
      "state_id": 0,
      "state_name": "",
      "state_code": ""
    }
  ],
  "status": "success",
  "has_more": 0,
  "has_total": 0,
  "user_has_addresses": true
},200)
            if args[0] == app.config['ZO_HOST'] + "/search":
                return MockResponse({
  "results_found": 26948,
  "results_start": 0,
  "results_shown": 1,
  "restaurants": [
    {
      "restaurant": {
        "R": {
          "has_menu_status": {
            "delivery": -1,
            "takeaway": -1
          },
          "res_id": 18560991
        },
        "apikey": "71ade8c61ec1c2ed4e98159f67a3d0ba",
        "id": "18560991",
        "name": "Lawless Burgerbar",
        "url": "https://www.zomato.com/jakarta/lawless-burgerbar-kemang?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "location": {
          "address": "Jl. Kemang Selatan VIII No. 67H-67I, Kemang, Jakarta",
          "locality": "Kemang",
          "city": "Jakarta",
          "city_id": 74,
          "latitude": "-6.2679110938",
          "longitude": "106.8144065514",
          "zipcode": "",
          "country_id": 94,
          "locality_verbose": "Kemang, Jakarta"
        },
        "switch_to_order_menu": 0,
        "cuisines": "Burger",
        "timings": "11h – 23h (Mon-Fri),11h – 24h (Sat),10h – 23h (Sun)",
        "average_cost_for_two": 150000,
        "price_range": 3,
        "currency": "IDR",
        "highlights": [
          "Credit Card",
          "Lunch",
          "Cash",
          "Debit Card",
          "Dinner",
          "Takeaway Available",
          "Beer",
          "Table booking recommended",
          "Wifi",
          "Outdoor Seating",
          "Indoor Seating",
          "Air Conditioned",
          "Smoking Area"
        ],
        "offers": [],
        "opentable_support": 0,
        "is_zomato_book_res": 0,
        "mezzo_provider": "OTHER",
        "is_book_form_web_view": 0,
        "book_form_web_view_url": "",
        "book_again_url": "",
        "thumb": "https://b.zmtcdn.com/data/pictures/chains/1/18560991/4467c4869a3fbb4bc1c16b95c8e82898.jpeg?fit=around%7C200%3A200&crop=200%3A200%3B%2A%2C%2A",
        "user_rating": {
          "aggregate_rating": "4.6",
          "rating_text": "Excellent",
          "rating_color": "3F7E00",
          "rating_obj": {
            "title": {
              "text": "4.6"
            },
            "bg_color": {
              "type": "lime",
              "tint": "800"
            }
          },
          "votes": "1813"
        },
        "all_reviews_count": 757,
        "photos_url": "https://www.zomato.com/jakarta/lawless-burgerbar-kemang/photos?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1#tabtop",
        "photo_count": 650,
        "photos": [
          {
            "photo": {
              "id": "u_zcwNjEwNDI1Njc",
              "url": "https://b.zmtcdn.com/data/reviews_photos/7a2/4915fc35a6795fe03a39d17fa32c97a2_1580199440.jpg",
              "thumb_url": "https://b.zmtcdn.com/data/reviews_photos/7a2/4915fc35a6795fe03a39d17fa32c97a2_1580199440.jpg?impolicy=newcropandfit&cropw=3024&croph=3024&cropoffsetx=0&cropoffsety=1008&cropgravity=NorthWest&fitw=200&fith=200&fittype=ignore",
              "user": {
                "name": "@OPPAKULINER",
                "zomato_handle": "Salim_moses",
                "foodie_level": "Connoisseur",
                "foodie_level_num": 13,
                "foodie_color": "e95151",
                "profile_url": "https://www.zomato.com/Salim_moses?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
                "profile_image": "https://b.zmtcdn.com/data/user_profile_pictures/f45/0906a019e3bda0fcc204a2a9c0557f45.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A",
                "profile_deeplink": "zomato://u/31082953"
              },
              "res_id": 18560991,
              "caption": "",
              "timestamp": 1580199442,
              "friendly_time": "2 months ago",
              "width": 3024,
              "height": 4032
            }
          },
          {
            "photo": {
              "id": "u_zODg4MDY1ODc3N",
              "url": "https://b.zmtcdn.com/data/reviews_photos/bcd/1174a8f42191bf58a24e37e6a667abcd_1571119480.jpg",
              "thumb_url": "https://b.zmtcdn.com/data/reviews_photos/bcd/1174a8f42191bf58a24e37e6a667abcd_1571119480.jpg?impolicy=newcropandfit&cropw=1440&croph=1440&cropoffsetx=0&cropoffsety=172&cropgravity=NorthWest&fitw=200&fith=200&fittype=ignore",
              "user": {
                "name": "Thomas Teguh",
                "zomato_handle": "Assygonz",
                "foodie_level": "Super Foodie",
                "foodie_level_num": 8,
                "foodie_color": "f58552",
                "profile_url": "https://www.zomato.com/Assygonz?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
                "profile_image": "https://b.zmtcdn.com/data/user_profile_pictures/a33/cabfeefff8e8445530efe27cdc286a33.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A",
                "profile_deeplink": "zomato://u/15809838"
              },
              "res_id": 18560991,
              "caption": "",
              "timestamp": 1571119480,
              "friendly_time": "6 months ago",
              "width": 1440,
              "height": 1800
            }
          },
          {
            "photo": {
              "id": "u_MDY4MTANjAwMjg",
              "url": "https://b.zmtcdn.com/data/reviews_photos/72b/20f09f7b0c1f324e59acf9e5a173272b_1571119480.jpg",
              "thumb_url": "https://b.zmtcdn.com/data/reviews_photos/72b/20f09f7b0c1f324e59acf9e5a173272b_1571119480.jpg?impolicy=newcropandfit&cropw=1440&croph=1440&cropoffsetx=0&cropoffsety=349&cropgravity=NorthWest&fitw=200&fith=200&fittype=ignore",
              "user": {
                "name": "Thomas Teguh",
                "zomato_handle": "Assygonz",
                "foodie_level": "Super Foodie",
                "foodie_level_num": 8,
                "foodie_color": "f58552",
                "profile_url": "https://www.zomato.com/Assygonz?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
                "profile_image": "https://b.zmtcdn.com/data/user_profile_pictures/a33/cabfeefff8e8445530efe27cdc286a33.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A",
                "profile_deeplink": "zomato://u/15809838"
              },
              "res_id": 18560991,
              "caption": "",
              "timestamp": 1571119480,
              "friendly_time": "6 months ago",
              "width": 1440,
              "height": 1800
            }
          },
          {
            "photo": {
              "id": "u_A5MzEyNjQ3OANj",
              "url": "https://b.zmtcdn.com/data/reviews_photos/2b9/04513f69d514d0729ed10e7ab6a4c2b9_1578039869.jpg",
              "thumb_url": "https://b.zmtcdn.com/data/reviews_photos/2b9/04513f69d514d0729ed10e7ab6a4c2b9_1578039869.jpg?impolicy=newcropandfit&cropw=3024&croph=3024&cropoffsetx=0&cropoffsety=640&cropgravity=NorthWest&fitw=200&fith=200&fittype=ignore",
              "user": {
                "name": "Cewek Rakus",
                "foodie_level": "Connoisseur",
                "foodie_level_num": 13,
                "foodie_color": "e95151",
                "profile_url": "https://www.zomato.com/users/cewek-rakus-50873671?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
                "profile_image": "https://b.zmtcdn.com/data/user_profile_pictures/3f3/dddab5036eea9a795bb2b3cd8ed743f3.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A",
                "profile_deeplink": "zomato://u/50873671"
              },
              "res_id": 18560991,
              "caption": "",
              "timestamp": 1578039870,
              "friendly_time": "3 months ago",
              "width": 3024,
              "height": 4032
            }
          },
          {
            "photo": {
              "id": "u_MTA2OTI4OTY1Mj",
              "url": "https://b.zmtcdn.com/data/reviews_photos/3f2/3e8031f2e318228722761dc5c8df33f2_1573264208.jpg",
              "thumb_url": "https://b.zmtcdn.com/data/reviews_photos/3f2/3e8031f2e318228722761dc5c8df33f2_1573264208.jpg?impolicy=newcropandfit&cropw=864&croph=864&cropoffsetx=104&cropoffsety=0&cropgravity=NorthWest&fitw=200&fith=200&fittype=ignore",
              "user": {
                "name": "Hilda Riani",
                "zomato_handle": "hildaaa24",
                "foodie_level": "Super Foodie",
                "foodie_level_num": 11,
                "foodie_color": "f58552",
                "profile_url": "https://www.zomato.com/hildaaa24?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
                "profile_image": "https://b.zmtcdn.com/data/user_profile_pictures/7dd/17cbf6c2371f55b96dbf3a105cd747dd.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A",
                "profile_deeplink": "zomato://u/32973245"
              },
              "res_id": 18560991,
              "caption": "",
              "timestamp": 1573264208,
              "friendly_time": "5 months ago",
              "width": 1152,
              "height": 864
            }
          },
          {
            "photo": {
              "id": "u_MTY1ODU0OTQ3Mz",
              "url": "https://b.zmtcdn.com/data/reviews_photos/c78/db065d3f0de754e31960ff87f4343c78_1575804871.jpg",
              "thumb_url": "https://b.zmtcdn.com/data/reviews_photos/c78/db065d3f0de754e31960ff87f4343c78_1575804871.jpg?impolicy=newcropandfit&cropw=756&croph=756&cropoffsetx=0&cropoffsety=213&cropgravity=NorthWest&fitw=200&fith=200&fittype=ignore",
              "user": {
                "name": "ARZ",
                "zomato_handle": "",
                "foodie_level": "Connoisseur",
                "foodie_level_num": 12,
                "foodie_color": "e95151",
                "profile_url": "https://www.zomato.com/users/arz-32042530?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
                "profile_image": "https://b.zmtcdn.com/data/user_profile_pictures/35f/c8af8fca64c721155a47db202c51335f.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A",
                "profile_deeplink": "zomato://u/32042530"
              },
              "res_id": 18560991,
              "caption": "#motleyburg(single)",
              "timestamp": 1575804871,
              "friendly_time": "4 months ago",
              "width": 756,
              "height": 1008
            }
          },
          {
            "photo": {
              "id": "u_5MDg3NTExMzE0M",
              "url": "https://b.zmtcdn.com/data/reviews_photos/71b/d754b9e0ef86893ac0a559d06117e71b_1569498029.jpg",
              "thumb_url": "https://b.zmtcdn.com/data/reviews_photos/71b/d754b9e0ef86893ac0a559d06117e71b_1569498029.jpg?impolicy=newcropandfit&cropw=1124&croph=1124&cropoffsetx=299&cropoffsety=0&cropgravity=NorthWest&fitw=200&fith=200&fittype=ignore",
              "user": {
                "name": "Novi Rita",
                "foodie_level": "Super Foodie",
                "foodie_level_num": 8,
                "foodie_color": "f58552",
                "profile_url": "https://www.zomato.com/users/novi-rita-15829653?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
                "profile_image": "https://b.zmtcdn.com/data/user_profile_pictures/cf1/7f1dc55864f1933c5a35a99a7ffeccf1.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A",
                "profile_deeplink": "zomato://u/15829653"
              },
              "res_id": 18560991,
              "caption": "",
              "timestamp": 1569498029,
              "friendly_time": "6 months ago",
              "width": 1500,
              "height": 1124
            }
          },
          {
            "photo": {
              "id": "u_UxMDk3NjEwODM2",
              "url": "https://b.zmtcdn.com/data/reviews_photos/bc7/b967c8f53bc7ae004b4810c1305ebbc7_1573303399.jpg",
              "thumb_url": "https://b.zmtcdn.com/data/reviews_photos/bc7/b967c8f53bc7ae004b4810c1305ebbc7_1573303399.jpg?impolicy=newcropandfit&cropw=2448&croph=2448&cropoffsetx=0&cropoffsety=0&cropgravity=NorthWest&fitw=200&fith=200&fittype=ignore",
              "user": {
                "name": "Ratih.ayu",
                "zomato_handle": "",
                "foodie_level": "Foodie",
                "foodie_level_num": 3,
                "foodie_color": "ffd35d",
                "profile_url": "https://www.zomato.com/users/ratihayu-51200776?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
                "profile_image": "https://b.zmtcdn.com/data/user_profile_pictures/1ab/49f05cee1c66ced23f0fea932ff7b1ab.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A",
                "profile_deeplink": "zomato://u/51200776"
              },
              "res_id": 18560991,
              "caption": "",
              "timestamp": 1573303399,
              "friendly_time": "5 months ago",
              "width": 2448,
              "height": 2448
            }
          },
          {
            "photo": {
              "id": "u_NDEwMjU5OTgNTE",
              "url": "https://b.zmtcdn.com/data/reviews_photos/480/c13792926fb5e63f15e8c64dc8039480_1583085294.jpg",
              "thumb_url": "https://b.zmtcdn.com/data/reviews_photos/480/c13792926fb5e63f15e8c64dc8039480_1583085294.jpg?impolicy=newcropandfit&cropw=3024&croph=3024&cropoffsetx=0&cropoffsety=70&cropgravity=NorthWest&fitw=200&fith=200&fittype=ignore",
              "user": {
                "name": "Arsyafdh",
                "foodie_level": "Foodie",
                "foodie_level_num": 2,
                "foodie_color": "ffd35d",
                "profile_url": "https://www.zomato.com/users/arsyafdh-34313393?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
                "profile_image": "https://b.zmtcdn.com/images/user_avatars/cupcake.png?fit=around%7C200%3A200&crop=200%3A200%3B%2A%2C%2A",
                "profile_deeplink": "zomato://u/34313393"
              },
              "res_id": 18560991,
              "caption": "",
              "timestamp": 1583085295,
              "friendly_time": "one month ago",
              "width": 3024,
              "height": 4032
            }
          },
          {
            "photo": {
              "id": "u_OTQzNzg2ODQwMj",
              "url": "https://b.zmtcdn.com/data/reviews_photos/270/18b1a1432db06211d3df8db90781d270_1577642231.jpg",
              "thumb_url": "https://b.zmtcdn.com/data/reviews_photos/270/18b1a1432db06211d3df8db90781d270_1577642231.jpg?impolicy=newcropandfit&cropw=3024&croph=3024&cropoffsetx=0&cropoffsety=1008&cropgravity=NorthWest&fitw=200&fith=200&fittype=ignore",
              "user": {
                "name": "LickingFinger",
                "zomato_handle": "",
                "foodie_level": "Big Foodie",
                "foodie_level_num": 6,
                "foodie_color": "ffae4f",
                "profile_url": "https://www.zomato.com/users/lickingfinger-150826957?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
                "profile_image": "https://b.zmtcdn.com/data/user_profile_pictures/8c8/9615e34187c64f559c2990bbf843b8c8.jpg?fit=around%7C100%3A100&crop=100%3A100%3B%2A%2C%2A",
                "profile_deeplink": "zomato://u/150826957"
              },
              "res_id": 18560991,
              "caption": "",
              "timestamp": 1577642231,
              "friendly_time": "3 months ago",
              "width": 3024,
              "height": 4032
            }
          }
        ],
        "menu_url": "https://www.zomato.com/jakarta/lawless-burgerbar-kemang/menu?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1&openSwipeBox=menu&showMinimal=1#tabtop",
        "featured_image": "https://b.zmtcdn.com/data/pictures/chains/1/18560991/4467c4869a3fbb4bc1c16b95c8e82898.jpeg",
        "has_online_delivery": 0,
        "is_delivering_now": 0,
        "store_type": "",
        "include_bogo_offers": true,
        "deeplink": "zomato://restaurant/18560991",
        "is_table_reservation_supported": 0,
        "has_table_booking": 0,
        "events_url": "https://www.zomato.com/jakarta/lawless-burgerbar-kemang/events#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1",
        "phone_numbers": "0813 81121602",
        "all_reviews": {
          "reviews": [
            {
              "review": []
            },
            {
              "review": []
            },
            {
              "review": []
            },
            {
              "review": []
            },
            {
              "review": []
            }
          ]
        },
        "establishment": [
          "Casual Dining"
        ],
        "establishment_types": []
      }
    }
  ]
}   , 200)

        else:
            return MockResponse(None, 404)

    # @mock.patch('requests.post', side_effect=mocked_requests_post)
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @patch('blueprints.iploc.resources.IpLocation.get')
    def test_check_zomato_ip(self,ipmock, get_mock, client):
        ipmock.return_value = {
    "ip": "114.5.218.223",
    "hostname": "114-5-218-223.resources.indosat.com",
    "city": "Jakarta",
    "region": "Jakarta",
    "country": "ID",
    "loc": "-6.2146,106.8451",
    "org": "AS4761 INDOSAT Internet Network Provider",
    "timezone": "Asia/Jakarta"
}
        token = create_token()
        res = client.get(
            '/zomato',
            query_string={"ip": "114.5.218.223"}, 
            headers={'Authorization':'Bearer ' + token}
            )
        res_json = json.loads(res.data)
        assert res.status_code == 200

