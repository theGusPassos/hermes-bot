(ns hermes-api.service
  (:require [io.pedestal.http.route :refer [expand-routes]]))

(def common-interceptors [])

(defn ensure-up [request]
  {:status 200 :body {:up true}})

(def default-routes
  #{["/api"
     :get (conj common-interceptors
                ensure-up)
     :route-name :test]})

(def routes
  (expand-routes default-routes))