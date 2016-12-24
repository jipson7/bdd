(ns bdd.core 
  (:require [bdd.buckets :as buckets]
            [bdd.colours :as colours])
  (:gen-class))

(defn -main
  [& args]
  (do 
    (buckets/run) 
    (colours/run)))


