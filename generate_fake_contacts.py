#!/usr/bin/env python3
"""
Script para generar contactos ficticios siguiendo la plantilla CSV de Go High Level
y los principios MECE (Mutuamente Exclusivos, Colectivamente Exhaustivos)
"""

import csv
import random
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Tuple

class FakeContactGenerator:
    def __init__(self):
        # Datos base para generar contactos ficticios
        self.first_names = [
            "Ana", "Luis", "Marta", "Pedro", "Carmen", "Javier", "Isabel", "Carlos",
            "Elena", "Miguel", "Laura", "Antonio", "Sofia", "David", "Patricia", "Roberto",
            "Nuria", "Francisco", "Cristina", "Manuel", "Rosa", "Jose", "Maria", "Alberto",
            "Teresa", "Ramon", "Angela", "Fernando", "Monica", "Diego", "Silvia", "Victor"
        ]
        
        self.last_names = [
            "García", "Martínez", "López", "Sánchez", "Rodríguez", "Fernández", "González",
            "Pérez", "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", "Díaz", "Moreno",
            "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez", "Navarro", "Torres",
            "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Suárez"
        ]
        
        # Sectores de negocio (MECE - sin solapamientos)
        self.business_sectors = {
            "alimentación": ["Panadería", "Carnicería", "Pescadería", "Frutería", "Cafetería"],
            "servicios-profesionales": ["Consultoría", "Asesoría", "Despacho", "Estudio"],
            "comercio": ["Tienda", "Comercio", "Establecimiento", "Negocio"],
            "salud": ["Clínica", "Centro Médico", "Farmacia", "Consultorio"],
            "educación": ["Academia", "Centro de Formación", "Escuela", "Instituto"],
            "tecnología": ["Empresa de Software", "Startup", "Consultoría IT", "Desarrollo Web"],
            "inmobiliaria": ["Inmobiliaria", "Agencia", "Promotora", "Gestora"],
            "automoción": ["Taller", "Concesionario", "Autoescuela", "Servicio Técnico"],
            "servicios-legales": ["Bufete", "Despacho de Abogados", "Asesoría Legal"],
            "finanzas": ["Asesoría Financiera", "Gestoría", "Consultoría Fiscal"]
        }
        
        # Tipos de empresa (MECE)
        self.company_types = {
            "autónomo": "",
            "pyme": "S.L.",
            "empresa": "S.A.",
            "cooperativa": "Coop.",
            "asociación": "Asoc."
        }
        
        # Etiquetas por sector (MECE)
        self.sector_tags = {
            "alimentación": ["sector-alimentación", "pyme", "comercio-local"],
            "servicios-profesionales": ["servicios-profesionales", "consultoría", "asesoría"],
            "comercio": ["comercio", "retail", "pyme"],
            "salud": ["sector-salud", "sanidad", "bienestar"],
            "educación": ["educación", "formación", "enseñanza"],
            "tecnología": ["tecnología", "innovación", "digital"],
            "inmobiliaria": ["inmobiliaria", "construcción", "real-estate"],
            "automoción": ["automoción", "transporte", "vehículos"],
            "servicios-legales": ["servicios-legales", "jurídico", "legal"],
            "finanzas": ["finanzas", "fiscal", "contabilidad"]
        }
        
        # Estados del lead (MECE)
        self.lead_states = ["prospecto", "lead-calificado", "cliente-potencial", "cliente-activo"]
        
        # Dominios de email ficticios
        self.email_domains = [
            "gmail.com", "hotmail.com", "outlook.com", "yahoo.com",
            "empresa.es", "negocio.com", "consultoria.es", "servicios.com"
        ]
        
        # Prefijos telefónicos españoles
        self.phone_prefixes = ["+34"]
        
    def generate_contact_id(self) -> str:
        """Genera un ID único para el contacto"""
        return str(uuid.uuid4())[:20]
    
    def generate_name(self) -> Tuple[str, str]:
        """Genera nombre y apellidos únicos"""
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        return first_name, last_name
    
    def generate_business_info(self) -> Tuple[str, str, str]:
        """Genera información del negocio siguiendo MECE"""
        sector = random.choice(list(self.business_sectors.keys()))
        business_type = random.choice(list(self.company_types.keys()))
        
        if business_type == "autónomo":
            business_name = f"{random.choice(self.business_sectors[sector])} {random.choice(self.first_names)}"
            company_name = ""
        else:
            business_name = f"{random.choice(self.business_sectors[sector])} {random.choice(self.last_names)}"
            company_name = f"{business_name} {self.company_types[business_type]}"
        
        return business_name, company_name, sector
    
    def generate_phone(self) -> str:
        """Genera un número de teléfono único"""
        prefix = random.choice(self.phone_prefixes)
        number = random.randint(600000000, 699999999)
        return f"{prefix}{number}"
    
    def generate_email(self, first_name: str, last_name: str, business_name: str) -> str:
        """Genera un email único basado en el nombre y negocio"""
        domain = random.choice(self.email_domains)
        
        # Diferentes formatos de email para variedad
        email_formats = [
            f"{first_name.lower()}.{last_name.lower()}@{domain}",
            f"{first_name.lower()}{last_name.lower()}@{domain}",
            f"{first_name.lower()}@{business_name.lower().replace(' ', '')}.{domain.split('.')[-1]}",
            f"{first_name.lower()}{random.randint(1, 99)}@{domain}"
        ]
        
        return random.choice(email_formats)
    
    def generate_dates(self) -> Tuple[str, str]:
        """Genera fechas de creación y última actividad"""
        # Fecha de creación en los últimos 2 años
        days_ago = random.randint(1, 730)
        created_date = datetime.now() - timedelta(days=days_ago)
        
        # Última actividad (70% de probabilidad de tener actividad)
        has_activity = random.random() < 0.7
        if has_activity:
            activity_days = random.randint(0, days_ago)
            last_activity = created_date + timedelta(days=activity_days)
        else:
            last_activity = ""
        
        created_str = created_date.strftime("%Y-%m-%dT%H:%M:%S+02:00")
        activity_str = last_activity.strftime("%Y-%m-%dT%H:%M:%S+02:00") if last_activity else ""
        
        return created_str, activity_str
    
    def generate_tags(self, sector: str, business_type: str) -> str:
        """Genera etiquetas siguiendo MECE"""
        tags = self.sector_tags[sector].copy()
        
        # Añadir etiqueta de tipo de empresa
        if business_type == "autónomo":
            tags.append("autónomo")
        else:
            tags.append("empresa")
        
        # Añadir estado del lead
        tags.append(random.choice(self.lead_states))
        
        # Añadir etiquetas adicionales específicas del sector
        if sector == "tecnología":
            tags.extend(["startup", "innovación"])
        elif sector == "salud":
            tags.extend(["sanidad", "bienestar"])
        elif sector == "finanzas":
            tags.extend(["fiscal", "contabilidad"])
        
        return ", ".join(tags)
    
    def generate_additional_emails(self, first_name: str, last_name: str) -> str:
        """Genera emails adicionales (30% de probabilidad)"""
        if random.random() < 0.3:
            domain = random.choice(self.email_domains)
            return f"{first_name.lower()}{random.randint(100, 999)}@{domain}"
        return ""
    
    def generate_additional_phones(self) -> str:
        """Genera teléfonos adicionales (20% de probabilidad)"""
        if random.random() < 0.2:
            prefix = random.choice(self.phone_prefixes)
            number = random.randint(600000000, 699999999)
            return f"{prefix}{number}"
        return ""
    
    def generate_contact(self) -> Dict[str, str]:
        """Genera un contacto completo"""
        first_name, last_name = self.generate_name()
        business_name, company_name, sector = self.generate_business_info()
        business_type = "autónomo" if not company_name else "empresa"
        
        contact = {
            "Contact Id": self.generate_contact_id(),
            "First Name": first_name,
            "Last Name": last_name,
            "Business Name": business_name,
            "Company Name": company_name,
            "Phone": self.generate_phone(),
            "Email": self.generate_email(first_name, last_name, business_name),
            "Created": self.generate_dates()[0],
            "Last Activity": self.generate_dates()[1],
            "Tags": self.generate_tags(sector, business_type),
            "Additional Emails": self.generate_additional_emails(first_name, last_name),
            "Additional Phones": self.generate_additional_phones()
        }
        
        return contact
    
    def generate_contacts_file(self, filename: str, num_contacts: int = 100):
        """Genera un archivo CSV con contactos ficticios"""
        fieldnames = [
            "Contact Id", "First Name", "Last Name", "Business Name", "Company Name",
            "Phone", "Email", "Created", "Last Activity", "Tags", "Additional Emails", "Additional Phones"
        ]
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            # Generar contactos únicos
            generated_contacts = set()
            contacts_generated = 0
            
            while contacts_generated < num_contacts:
                contact = self.generate_contact()
                
                # Verificar que el email sea único
                email_key = contact["Email"]
                if email_key not in generated_contacts:
                    generated_contacts.add(email_key)
                    writer.writerow(contact)
                    contacts_generated += 1
                    
                    if contacts_generated % 10 == 0:
                        print(f"Generados {contacts_generated} contactos...")
        
        print(f"Archivo '{filename}' generado exitosamente con {num_contacts} contactos únicos.")

def main():
    """Función principal"""
    print("Generador de Contactos Ficticios MECE")
    print("=====================================")
    
    # Crear instancia del generador
    generator = FakeContactGenerator()
    
    # Solicitar número de contactos
    try:
        num_contacts = int(input("¿Cuántos contactos quieres generar? (por defecto 100): ") or "100")
    except ValueError:
        num_contacts = 100
        print("Valor inválido, usando 100 contactos por defecto.")
    
    # Generar archivo
    filename = f"contactos_ficticios_mece_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    generator.generate_contacts_file(filename, num_contacts)
    
    print(f"\nArchivo generado: {filename}")
    print("Los contactos siguen los principios MECE:")
    print("- Mutuamente Exclusivos: Cada categoría es independiente")
    print("- Colectivamente Exhaustivos: Cubren todos los sectores relevantes")

if __name__ == "__main__":
    main()
