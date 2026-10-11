#!/usr/bin/env python3
"""Run the guarded SLP driver on the corrected rail-preserving endpoint."""
import slp_search as driver
import rail_combined_core as corrected_core

driver.core = corrected_core

if __name__ == "__main__":
    driver.main()
