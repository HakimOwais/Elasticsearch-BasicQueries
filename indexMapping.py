indexMapping = {
    "properties":{
        "Job.ID":{
            "type":"long"
        },
        "Status":{
            "type":"text"
        },
        "Title":{
            "type":"text"
        },
        "Position":{
            "type":"text"
        },
        "Company":{
            "type":"keyword"
        },
        "Job.Description":{
            "type":"keyword"
        },
        "Education.Required":{
            "type":"text"
        },
        "Employment.Type":{
            "type":"text"
        },
        "Industry":{
            "type":"text"
        },
        "JobDescriptionVector":{
            "type":"dense_vector",
            "dims": 768,
            "index":True,
            "similarity": "l2_norm"
        }

    }
}