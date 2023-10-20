from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, SystemBoundary, Relationship
from diagrams.onprem.queue import Kafka

with Diagram("Container diagram for Reservation Resource System"):
    customer = Person(
        name="User", description="A client who needs to book some resource for a certain period of time"
    )

    with SystemBoundary("Reservation Resource System"):

        spa = Container(
            name="Web Application",
            technology="SPA",
            description="application on any SPA framework",
        )

        #api/resources/v1 [GET]
        #api/resources/v1/create [POST]
        #api/resources/v1/{id} [GET]
        #api/resources/v1/{id}/delete [POST]
        #api/booking/v1 [GET] 
        #api/booking/v1/create [POST]
        #api/booking/v1/{id} [GET] 
        #api/booking/v1/{id}/release [POST]
        #api/booking/v1/{id}/history [GET]
        #api/booking/v1/byresource?res_id= [GET] 
        #api/booking/v1/bytimerange?from=;to= [GET] 
        api = Container(
            name="api-gateway",
            technology="Java and Spring MVC",
            description="Provides resource and bookings management via a JSON/HTTPS API.",
        )
        
        with SystemBoundary("Resource service"):
                  
            resource_service = Container(
                name="resource-svc",
                technology="Golang",
                description="Master system of resources"
            )
            
            resource_db = Database(
                name="resource-db", 
                technology="postgres", 
                description="store state, metadata of resources"
            )
            resource_topic = Kafka("resource-events")
            
        with SystemBoundary("Booking service"):
                  
            booking_service = Container(
                name="bookings-svc",
                technology="Golang",
                description="Master system of bookings"
            )
            
            booking_db = Database(
                name="booking-db", 
                technology="postgres", 
                description="store state & metadata of bookings"
            )
            booking_topic = Kafka("booking-events")
    
    customer >> Relationship("Views, creates and manage of resource and bookings") >> [spa]
    spa >> Relationship("Make API calls to [JSON/HTTPS]") >> api        
    api >> Relationship("Make API calls to [gRPC]") >> resource_service
    api >> Relationship("Make API calls to [gRPC]") >> booking_service
    resource_service >> Relationship("Store and Query data of resources") >> resource_db
    resource_service >> Relationship("Produce remove resource events") >> resource_topic
    resource_topic >> Relationship("Consume events about remove resource operation") >> booking_service
    booking_service >> Relationship("Store and Query data of bookings") >> booking_db
    booking_service >> Relationship("Produce booking state changes events") >> booking_topic
    booking_topic >> Relationship("Consume events about booking state changes") >> resource_service
    
    
    
