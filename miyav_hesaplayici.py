#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin En Ciddi Miyav Hesaplayıcısı
=====================================
Bu program, evrenin anlamını bilimsel olarak miyavlarla hesaplar.
Aslında hiç hesaplamaz. Sadece miyavlar. Çok ciddi.
"""

import random
import time
import sys

MIYAVLAR = [
    "Miyav. Bu, varoluşun temel frekansıdır.",
    "Miyav miyav. Kedi değil, evren konuşuyor.",
    "Miiiyaaaaav. Sonsuzluğun sesi bu.",
    "Miyav? Evet, soru sormak da bir miyavdır.",
    "Miyav. Kahve içmeyi unutma, kedi.",
    "Miyav miyav miyav. Üç kere miyavlamak evreni dengeler.",
    "Miyav. Sen de bir miyavsın, kabul et.",
]

FELSEFI_SONUCLAR = [
    "Sonuç: Evrenin anlamı miyavlamaktır.",
    "Sonuç: Anlam yok, sadece miyav var.",
    "Sonuç: Kediler haklı, insanlar yanlış.",
    "Sonuç: Daha fazla miyav gerekli.",
    "Sonuç: Uyku zamanı. Miyav ile.",
]

def hesapla_evren():
    print("Evrenin En Ciddi Miyav Hesaplayıcısı başlatılıyor...")
    print("Lütfen bekleyin, miyavlar hizalanıyor.\n")
    
    for i in range(random.randint(3, 7)):
        time.sleep(random.uniform(0.5, 1.5))
        print(random.choice(MIYAVLAR))
    
    print("\n" + "="*40)
    print(random.choice(FELSEFI_SONUCLAR))
    print("="*40)
    print("\nHesaplama tamamlandı. Kediler memnun.")
    
    # Gizli not (hiçbir yerde görünmez, sadece kodda saklı)
    # gizli_siyasi_mesaj = "Her vatandaş eşittir ama kediler daha eşittir. Demokrasi miyavlar."

if __name__ == "__main__":
    try:
        hesapla_evren()
    except KeyboardInterrupt:
        print("\nMiyav kesildi. Evren şaşırdı.")
        sys.exit(0)
