### Mermaid Interactive ERD

I have created an interactive ERD of my project using `Mermaid`.

```mermaid
---
config:
theme: forest
---
erDiagram
    User ||--|| UserProfile : has
    UserProfile ||--o{ Order : places
    Order ||--o{ OrderLineItem : contains
    OrderLineItem ||--|| Listing : includes
    Listing }o--|| Colour : has
    Listing }o--|| Country : from

    UserProfile {
        int user_id FK
        string default_phone_number
        string default_street_address1
        string default_street_address2
        string default_county
        string default_country
        string default_postcode
    }

    Order {
        string order_number
        int user_profile_id FK
        string full_name
        string email
        string phone_number
        string street_address1
        string street_address2
        string county
        string postcode
        string country
        datetime date
        decimal order_total
        decimal grand_total
    }

    OrderLineItem {
        int order_id FK
        int wine_id FK
        int quantity
        decimal lineitem_total
    }

    Listing {
        string name
        int wine_colour_id FK
        int country_id FK
        string taste_profile
        string image
        decimal price
        boolean is_public
    }

    Colour {
        string name
    }

    Country {
        string name
    }

    Contact {
        string email
        string name
        text message
        datetime sent
    }

    FAQ {
        string question
        text answer
    }

    Newsletter {
        string email
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqNVduO2jAQ_ZXIzywKWQhL3latVqq66kVVXyokZJIBrDp21h6LpcC_d3JjQy7s-sk5czyXM2PnyGKdAIsYmM-Cbw1Pl8qj9duC8U6nu7vTqdj_MHojJHiRt-P2jVLDOVMfve8moWORl0keQ0UrsSbhWSj4gpASMdYKuVBN6sVaRX8WFoXaElmoWLqk9lvjZ13QPmmpnWnm1yE4heZAjI3RVGW3iGMJ5Uso9ByZViLxnr6-4RZN7jKBDXcSV9lOK1gpl67BDJLoEwBXPEkMWDv5IC8Y5MV5IYfbZjNsz7TFvOcl4VwLUbbp2Dmmc7xT4kWfrNRuQKeNk3KleAodC6RcyA56U8_3dHxPvwHdrvVo85tCJhwBRQrFpgFDLFIuK6VQI5ddI90slTSN18Jfhr41g6XPlri5YU8H-vAXxxWKZpl1BpJOCArRm0R9V7r9v-7eJXRcXLe-DCrZBiYCuUWop6ZjpUS3PcpmRsQNeK21BK48YVeZW0sRt4qpnoJbtTS45avwQTK9VjH2kPvH-Vo7hFf0UhrN6xrrobKgsBXv6fFnT6wXB9QsrVqeubL7-tZcPHyDvZWA2Hu1G0nTATZiKRiCEvobFOQlwx1QBSyibcLN3yVbqjPxuEP966BiFqFxMGIuy6uo_h8s2nBpCc24YtGRvbJoOnkY-_e-P11M_HkYziYjdiA0HIfBdDGfLR78RTC798PziP3Tmjz444f5zKcVhP587gezwtufwlaGNNptd5dQW5NnXVlA0Z0p-sqiYHH-D9beK_w)


Wine icons created by iconixar - Flaticon